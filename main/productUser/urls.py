from django.urls import path

from .views import ProductUserViewSet


urlpatterns = [
    path('prod_user', ProductUserViewSet.as_view({
        'get' : 'list',
    })),
]