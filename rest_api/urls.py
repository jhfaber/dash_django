from django.shortcuts import render

# Create your views here.

from django.urls import path

from . import views
# from rest_framework import routers

# from .viewsets import ElementViewSet
from .models import Element, Category,TypeElement

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields='__all__'
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TypeElementSerializer(serializers.ModelSerializer):
    class Meta:
        model= TypeElement
        fields='__all__'
class TypeElementViewSet(viewsets.ModelViewSet):
    queryset = TypeElement.objects.all()
    serializer_class = TypeElementSerializer


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model= Element
        fields='__all__'
class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


router =routers.SimpleRouter()
router.register(r'element',ElementViewSet)
router.register(r'tipeelement',TypeElementViewSet)
router.register(r'category',CategoryViewSet)

# app_name = 'rest_api'
urlpatterns = router.urls
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('rest_api/', include('rest_api.urls', namespace='rest_framework'))
# ]