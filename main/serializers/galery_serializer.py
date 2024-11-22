from rest_framework import serializers

from main.models.galery import Galery
from main.models.image import ImageField
from main.serializers.image_serializer import ImageSerializer

class GalerySerializer(serializers.ModelSerializer):
    img = ImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Galery
        fields = '__all__'
        
class GallerySerializerPost(serializers.ModelSerializer):
    img = serializers.PrimaryKeyRelatedField(many=True, queryset=ImageField.objects.all())
    
    def get_image_pks(self, obj):
        return [img.pk for img in obj.img.all()]
    
    class Meta:
        model = Galery
        fields = '__all__'