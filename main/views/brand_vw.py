from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from main.models.brand import Brand
from main.serializers.brand_serializer import BrandSerializer

class BrandViewset(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    