
from rest_framework import viewsets
from rest_framework.response import Response
from main.models.image import ImageField
from main.serializers.image_serializer import ImageSerializer

class ImageViewset(viewsets.ModelViewSet):
    queryset = ImageField.objects.all()
    serializer_class = ImageSerializer 
    
    def create(self, request, *args, **kwargs):
        data = request.data
        data_type = data.get('type')
        if data_type:
            return super().create(request, *args, **kwargs)
        else:
            data["type"] = "product_img"
            image_serializer = ImageSerializer(data=request.data)
            image_serializer.is_valid(raise_exception=True)
            image_serializer.save()
            return Response(image_serializer.data)  