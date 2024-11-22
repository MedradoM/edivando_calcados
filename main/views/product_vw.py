
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from main.models.product import Product
from main.serializers.product_serializer import ProductSerializer, ProductSerializerPost
from rest_framework.response import Response
from rest_framework import status

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {"title": ["icontains"], "value": ["icontains"], "group__category__name": ["icontains"], "brand__name": ["icontains"]}

    # def get_queryset(self):
    #     queryset = super().get_queryset()

        
    #     return 

def get_serializer_class(self):
    if self.request.method in ['POST', 'PUT', 'PATCH']:
        return ProductSerializerPost
    return ProductSerializer

    # def create(self, request, *args, **kwargs):
    #     data = request.data

    #     if isinstance(data, list):
    #         data = data[0]  # Assuming you want to take the first dictionary in the list

    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     product = serializer.instance

    #     if 'brand_id' in data:
    #         product.brand_id.set(data['brand_id'])
    #     if 'group_id' in data:
    #         product.group_id.set(data['group_id'])
    #     if 'galery_id' in data:
    #         product.galery_id.set(data['galery_id'])
    #     product.save()

    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    # # def create(self, request, *args, **kwargs):
    # #     return super().create(request, *args, **kwargs)
    