from rest_framework import serializers

from .models import ProductUser

class ProductUserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    class Meta:
        model = ProductUser
        fields = '__all__'