from rest_framework import serializers

from main.models.brand import Brand
from main.models.galery import Galery
from main.models.group import GroupModel
from main.models.product import Product
from main.serializers.brand_serializer import BrandSerializer
from main.serializers.galery_serializer import GalerySerializer
from main.serializers.group_serializer import GroupSerializer  

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    galery = GalerySerializer(many=False, read_only=True)
    group = GroupSerializer(many=False, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductSerializerPost(serializers.ModelSerializer):
    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), source='brand')
    galery_id = serializers.PrimaryKeyRelatedField(queryset=Galery.objects.all(), source='galery')
    group_id = serializers.PrimaryKeyRelatedField(queryset=GroupModel.objects.all(), source='group')
    
    class Meta:
        model = Product
        fields = '__all__'