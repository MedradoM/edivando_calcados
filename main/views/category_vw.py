from rest_framework import viewsets

from main.models.category import Category
from main.serializers.category_serializer import CategorySerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
