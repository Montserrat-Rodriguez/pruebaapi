from rest_framework import routers, serializers

from django.contrib.auth.models import User

from example.models import User2
from example.models import Product

from example.models import Inventory
from example.models import Transaction

from example.models import Sale


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


class UseridSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username')

class ProductnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name')

class InventorySerializer(serializers.ModelSerializer):
    #usuarioI = UseridSerializer(many=True)
    #productoI = ProductidSerializer(many=True)
    class Meta:
        model = Inventory
        fields = ('__all__')

class InventoryviewSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='user_id.username')#UseridSerializer(many=True, read_only=True)
    producto = serializers.ReadOnlyField(source='product_id.name')#ProductnameSerializer(many=True, read_only=True)
    code = serializers.ReadOnlyField(source='product_id.code')
    status = serializers.ReadOnlyField(source='product_id.status')
    description = serializers.ReadOnlyField(source='product_id.description')
    class Meta:
        model = Inventory
        fields = ('__all__')
        #fields = ('__all__')

class TransactionviewSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='inventory_id.user_id.username')
    class Meta:
        model = Transaction
        fields = ('__all__')


class SalesviewSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='user_id.username')
    producto = serializers.ReadOnlyField(source='product_id.name')
    class Meta:
        model = Sale
        fields = ('__all__')
        
class InventoryidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id')



class TransactionSerializer(serializers.ModelSerializer):
    inventario = InventoryidSerializer(many=True)
    class Meta:
        model = Transaction
        fields = ('__all__')

class SaleSerializer(serializers.ModelSerializer):
    #usuarioI = UseridSerializer(many=True)
    #productoI = ProductidSerializer(many=True)
    class Meta:
        model = Sale
        fields = ('__all__')

