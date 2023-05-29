from django.urls import path

from .views import ProductUserViewSet


urlpatterns = [
    path('products', ProductUserViewSet.as_view({
        'get' : 'list',
    })),
    path('products/<str:id>/like', ProductUserViewSet.as_view({
        'post': 'like',
    })),
]