from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.urls import path

from . import views

from .models import Element, Category,TypeElement

from django.urls import path, include
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from comment_app.models import Comment




class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Category
        fields='__all__'


class CommentSerializer(serializers.ModelSerializer):


    # CUSTOM FIELD TAKES THE VALE OF GET_COUNT()
    count = serializers.SerializerMethodField()
    
    class Meta:
        model= Comment
        fields='__all__'

    def get_count(self, obj):
        print(obj)

        return Comment.objects.filter(element_id = obj.element_id).count()

class TypeElementSerializer(serializers.ModelSerializer):
    class Meta:
        model= TypeElement
        fields='__all__'


class ElementSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    # type_element = serializers.StringRelatedField()
    # comments = serializers.StringRelatedField(many=True)

    # This will created a structure of each object inside element
    category = CategorySerializer(read_only=True)
    type_element = TypeElementSerializer(read_only=True)
    comments =  CommentSerializer(many= True,read_only=True)
    
    # element = serializers.StringRelatedField()
    class Meta:
        model= Element
        fields='__all__'
        # fields = ['text']


###############################################3
#  VIEWSET
########################################


class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

    # Detail False is like many elements, true is 1 element
    @action(detail=False, methods=['get'])
    def all(self, request, pk=None):
        queryset = Element.objects.all()

        serializer = ElementSerializer(queryset,many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def url(self, request, ):
        queryset = Element.objects.all()
        print(request.query_params)
        # queryset = Element.objects.get(url_clean=request.query_params["url_clean"])
        
        # queryset = get_object_or_404(Element, url_clean=request.query_params["url_clean"])
        serializer = ElementSerializer(queryset,many=True)
        return Response(serializer.data)

    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # filter for getting one unique element additional action
    # http://127.0.0.1:8000/rest_api/category/2/elements
    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(category_id=pk)

        serializer = ElementSerializer(queryset,many=True)
        return Response(serializer.data)
        

class TypeElementViewSet(viewsets.ModelViewSet):
    queryset = TypeElement.objects.all()
    serializer_class = TypeElementSerializer

# READ ONLY DON'T ALLOW POST, PUT
class CommentViewSet(viewsets.ReadOnlyModelViewSet):
# class CommentViewSet(viewsets.ModelViewSet):
    # queryset = Comment.objects.all()

    # Brings not null
    queryset = Comment.objects.exclude(element__isnull=False)
    serializer_class = CommentSerializer


router =routers.SimpleRouter()
router.register(r'element',ElementViewSet)
router.register(r'tipeelement',TypeElementViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'comment',CommentViewSet)


urlpatterns = router.urls
# app_name = 'rest_api'

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('rest_api/', include('rest_api.urls', namespace='rest_framework'))
# ]