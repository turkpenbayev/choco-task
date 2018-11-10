from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import *
from .serializers import *

# Create your views here.
class SalonsView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        salon = Salon.objects.all()
        serializer = SalonSerializers(salon, many = True)
        return Response({'data': serializer.data})

class CreateUsersView(CreateAPIView):

    permission_classes = [permissions.AllowAny]
    
    model = User
    serializer_class = UserCreateSerializers


class UsersView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        users = User.objects.all()
        serializer = UserSerializers(users, many = True)

        return Response({'data': serializer.data})


