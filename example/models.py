from django.db import models
from django.contrib.auth.models import User

# Create your views here.

class Example(models.Model):
    
    class Meta:
        db_table = "Example"

class User2(models.Model):
    username = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=50, null=False)
    rol = models.IntegerField( null=False )
    is_superuser = models.IntegerField(null=False)

    class Meta:
        db_table = "users"


#modelo extra

class Product(models.Model):
    code = models.CharField(max_length=30, null=False, unique=True)
    name = models.CharField(max_length=30, default=False, null=False)
    description = models.CharField(max_length = 255, null = False)
    image = models.CharField(max_length=150, null=False)
    status = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = "products"

class Inventory(models.Model):
    product_id= models.ForeignKey(Product, on_delete=models.SET(-1))#, related_name='productoI'
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    user_id = models.ForeignKey(User, on_delete=models.SET(-1))#, related_name='usuarioI'
    tax = models.FloatField(null=False)

    class Meta:
        db_table = "inventories"

class Transaction(models.Model):
    inventory_id = models.ForeignKey(Inventory, on_delete=models.SET(-1))#, related_name='inventario'
    date = models.DateField(null=False)
    typee = models.CharField(max_length=30, null=False)

    class Meta:
        db_table = "transactions"

class Sale(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET(-1))#, related_name='productS'
    user_id = models.ForeignKey(User, on_delete=models.SET(-1))#, related_name='userSe'
    quantity = models.IntegerField(null=False)
    discount = models.FloatField(null=False )
    total = models.FloatField(null=False)
    date = models.DateField(null=False)
    status = models.CharField(max_length=30, null=False)
    paymaneth_method=models.IntegerField(null=False)

    class Meta:
        db_table = "sales"

