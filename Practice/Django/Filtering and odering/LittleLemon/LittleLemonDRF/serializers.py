from rest_framework import serializers
# from rest_framework.fields import IntegerFeild
from .models import MenuItem, Category

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class MenuItemSerializer(serializers.ModelSerializer) :
    category_id = serializers.IntegerFeild(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = [
            'id',
            'title',
            'price',
            'inventory',
            'category',
            'category_id'
        ]