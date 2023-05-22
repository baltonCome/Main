from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ProductUser, Product
from .serializers import ProductUserSerializer


class ProductUserViewSet(viewsets.ViewSet):
    def list(self, request):
        prod_user = ProductUser.objects.all()
        serializer = ProductUserSerializer(prod_user) 
        return Response(serializer.data, 200) 
    
    