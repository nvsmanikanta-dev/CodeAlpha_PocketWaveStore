from django.contrib import messages
from decimal import Decimal
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.utils.http import url_has_allowed_host_and_scheme
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CheckoutForm, RegisterForm
from .models import Order, OrderItem, Product

def home(request):
    products=Product.objects.filter(is_active=True).order_by('id')[:6]
    return render(request,'store/home.html',{'products':products})

def product_list(request):
    products=Product.objects.filter(is_active=True)
    q=request.GET.get('q','').strip()[:100]; category=request.GET.get('category','').strip()
    if q: products=products.filter(Q(name__icontains=q)|Q(description__icontains=q)|Q(category__icontains=q))
    if category: products=products.filter(category=category)
    sort=request.GET.get('sort','featured')
    sort_fields={'featured':'id','price_asc':'price','price_desc':'-price','newest':'-created_at'}
    products=products.order_by(sort_fields.get(sort,'id'))
    categories=Product.objects.filter(is_active=True).values_list('category',flat=True).distinct().order_by('category')
    return render(request,'store/product_list.html',{'products':products,'categories':categories,'q':q,'selected_category':category,'sort':sort})

def product_detail(request,slug):
    product=get_object_or_404(Product,slug=slug,is_active=True)
    return render(request,'store/product_detail.html',{'product':product})

def register_view(request):
    if request.user.is_authenticated: return redirect('home')
    form=RegisterForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        user=form.save(); login(request,user); messages.success(request,'Account created successfully.'); return redirect('home')
    return render(request,'registration/register.html',{'form':form})

def cart_detail(request): return render(request,'store/cart.html',{'cart':Cart(request)})

@require_POST
def cart_add(request,product_id):
    product=get_object_or_404(Product,id=product_id,is_active=True)
    try: qty=max(1,int(request.POST.get('quantity',1)))
    except (TypeError,ValueError): qty=1
    if product.stock<1: messages.error(request,'This product is out of stock.')
    else: Cart(request).add(product,qty); messages.success(request,f'{product.name} added to cart.')
    next_url=request.POST.get('next','')
    return redirect(next_url if url_has_allowed_host_and_scheme(next_url,{request.get_host()}) else 'cart')

@require_POST
def cart_update(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    try: qty=int(request.POST.get('quantity',1))
    except (TypeError,ValueError): qty=1
    qty=min(max(qty,0),product.stock)
    Cart(request).add(product,qty,override=True); return redirect('cart')

@require_POST
def cart_remove(request,product_id):
    Cart(request).remove(get_object_or_404(Product,id=product_id)); return redirect('cart')

@login_required
def checkout(request):
    cart=Cart(request)
    if len(cart)==0: messages.info(request,'Your cart is empty.'); return redirect('products')
    initial={'full_name':request.user.get_full_name() or request.user.username,'email':request.user.email}
    form=CheckoutForm(request.POST or None,initial=initial)
    if request.method=='POST' and form.is_valid():
        rows=list(cart)
        with transaction.atomic():
            locked={p.id:p for p in Product.objects.select_for_update().filter(id__in=[row['product'].id for row in rows],is_active=True)}
            for row in rows:
                p=locked.get(row['product'].id)
                if p is None or row['quantity']>p.stock:
                    messages.error(request,'The stock for an item changed. Please review your bag.')
                    return redirect('cart')
            order=form.save(commit=False); order.user=request.user
            order.total_amount=sum((locked[row['product'].id].price*row['quantity'] for row in rows), Decimal('0'))
            order.save()
            for row in rows:
                p=locked[row['product'].id]
                OrderItem.objects.create(order=order,product=p,product_name=p.name,price=p.price,quantity=row['quantity'])
                p.stock-=row['quantity']; p.save(update_fields=['stock'])
        cart.clear(); messages.success(request,f'Order #{order.id} placed successfully!'); return redirect('order_success',order_id=order.id)
    return render(request,'store/checkout.html',{'cart':cart,'form':form})

@login_required
def order_success(request,order_id):
    order=get_object_or_404(Order,id=order_id,user=request.user)
    return render(request,'store/order_success.html',{'order':order})

@login_required
def order_history(request):
    return render(request,'store/order_history.html',{'orders':request.user.orders.prefetch_related('items').order_by('-created_at')})
