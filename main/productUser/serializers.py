from rest_framework import serializers

from .models import ProductUser

class ProductUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUser
        fields = '__all__'