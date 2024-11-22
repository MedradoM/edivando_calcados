from rest_framework import serializers

from main.models.image import ImageField 

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageField
        fields = '__all__'