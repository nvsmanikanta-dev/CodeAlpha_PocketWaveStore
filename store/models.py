from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name=models.CharField(max_length=160)
    slug=models.SlugField(unique=True)
    category=models.CharField(max_length=80)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    image_url=models.URLField(blank=True)
    image_asset=models.CharField(max_length=120,blank=True,default='img/products/phone-generic.svg')
    brand=models.CharField(max_length=60,blank=True)
    storage=models.CharField(max_length=50,blank=True)
    display=models.CharField(max_length=60,blank=True)
    battery=models.CharField(max_length=60,blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class Order(models.Model):
    STATUS_CHOICES=[('PLACED','Placed'),('PROCESSING','Processing'),('SHIPPED','Shipped'),('DELIVERED','Delivered'),('CANCELLED','Cancelled')]
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    full_name=models.CharField(max_length=120)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    address=models.TextField()
    city=models.CharField(max_length=80)
    pincode=models.CharField(max_length=12)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='PLACED')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'Order #{self.pk} - {self.user.username}'

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    product_name=models.CharField(max_length=160)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField()
    def subtotal(self): return self.price*self.quantity
