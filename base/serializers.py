# serializers.py
from rest_framework import serializers
from .models import Product , Students
# 2.first step

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'desc', 'price', 'createdTime']

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
