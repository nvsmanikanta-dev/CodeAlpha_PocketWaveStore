from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Product, Order

class StoreFlowTests(TestCase):
    def setUp(self):
        self.product=Product.objects.create(name='Test Product',slug='test-product',category='Test',description='Demo',price='100.00',stock=5,is_active=True)
        self.user=User.objects.create_user(username='tester',password='StrongPass123',email='test@example.com')

    def test_product_pages(self):
        self.assertEqual(self.client.get(reverse('products')).status_code,200)
        self.assertContains(self.client.get(reverse('product_detail',args=[self.product.slug])),'Test Product')

    def test_cart_add(self):
        response=self.client.post(reverse('cart_add',args=[self.product.id]),{'quantity':2})
        self.assertEqual(response.status_code,302)
        self.assertEqual(self.client.session['cart'][str(self.product.id)]['quantity'],2)

    def test_cart_never_exceeds_available_stock(self):
        self.client.post(reverse('cart_add',args=[self.product.id]),{'quantity':4})
        self.client.post(reverse('cart_add',args=[self.product.id]),{'quantity':4})
        self.assertEqual(self.client.session['cart'][str(self.product.id)]['quantity'],5)

    def test_checkout_creates_order_and_updates_stock(self):
        self.client.login(username='tester',password='StrongPass123')
        self.client.post(reverse('cart_add',args=[self.product.id]),{'quantity':2})
        response=self.client.post(reverse('checkout'),{'full_name':'Test User','email':'test@example.com','phone':'9999999999','address':'Test Address','city':'Vijayawada','pincode':'520001'})
        self.assertEqual(response.status_code,302)
        order=Order.objects.get(user=self.user)
        self.assertEqual(order.items.count(),1)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock,3)
