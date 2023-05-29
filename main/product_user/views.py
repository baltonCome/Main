from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from .models import ProductUser, Product
from .serializers import ProductUserSerializer
from .producer import publish


class ProductUserViewSet(viewsets.ViewSet):
    def list(self, request):
        prod_user = ProductUser.objects.all()
        serializer = ProductUserSerializer(prod_user, many = True) 
        return Response(serializer.data, 200) 

    def like(self, request, id):
        request = requests.get('http://host.docker.internal:8000/api/user')
        json_data = request.json()

        try: 
            product_user = ProductUser(user_id=json_data['id'],product_id=id)
            product_user.save()

            publish('product_liked', id)
        except: 
            return JsonResponse({'message': 'You already liked this product'}, status=400)

        return Response(json_data, 200)
