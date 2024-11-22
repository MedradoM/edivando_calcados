from rest_framework import serializers

from main.models.category import Category
from main.models.group import GroupModel
from main.serializers.category_serializer import CategorySerializer

class GroupSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=False)
    
    class Meta:
        model = GroupModel
        fields = '__all__'
        
class GroupSerializerPost(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
    
    class Meta:
        model = GroupModel
        fields = '__all__'