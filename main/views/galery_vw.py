
from rest_framework import viewsets

from main.models.galery import Galery
from main.serializers.galery_serializer import GalerySerializer, GallerySerializerPost
from rest_framework.response import Response
from rest_framework import status

class GaleryViewset(viewsets.ModelViewSet):
    queryset = Galery.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return GallerySerializerPost
        return GalerySerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            img_pks = request.data
            data = {
                "name": "Default Name",
                "img": img_pks
            }
        else:
            data = request.data

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        galery = serializer.instance

        if 'img' in data:
            galery.img.set(data['img'])
            galery.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()