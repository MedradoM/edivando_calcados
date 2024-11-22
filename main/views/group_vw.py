
from rest_framework import viewsets

from main.models.group import GroupModel
from main.serializers.group_serializer import GroupSerializer, GroupSerializerPost

class GroupViewset(viewsets.ModelViewSet):
    queryset = GroupModel.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return GroupSerializerPost
        return GroupSerializer
    