from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import *
from .serializers import (SalonSerializers, ServiceSerializers, UserCreateSerializers, 
UserSerializers, ProfileSerializers)

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

class ServicesView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        service = Service.objects.all()
        serializer = ServiceSerializers(service, many = True)
        return Response({'data': serializer.data})


class ProfilesView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    

    def get(self, request):
        profile = Profile.objects.get(user = request.user)
        serializer = ProfileSerializers(profile)
        return Response({'data': serializer.data})

    def post(self, request):
        user = request.user
        profile = ProfileSerializers(data = request.data)

        if profile.is_valid():
            profile.save(user = request.user)
            return Response({'status': 'Added proflie'})
        else:
            return Response({'status': 'Error'})
    
    def put(self, request, format=None):
        profile = request.user.profile
        serializer = ProfileSerializers(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

