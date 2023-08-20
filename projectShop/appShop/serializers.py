
from django.db.models import fields
from rest_framework import serializers
from .models import Category
 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category', 'subcategory', 'name', 'amount')