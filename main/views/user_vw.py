from django.shortcuts import render
from rest_framework.decorators import action

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets

from main.serializers.user_serializer import UserSerializer

class UserViewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["get"])
    def me(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)