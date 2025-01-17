from rest_framework import serializers
from rest_framework.serializers import FileField

from main.models.brand import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
