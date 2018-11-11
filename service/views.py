from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import *
from .serializers import (SalonSerializers, ServiceSerializers, UserCreateSerializers, 
UserSerializers, ProfileSerializers, MasterSerializers, OrderSerializers, OrderPostSerializers)

# Create your views here.
class SalonView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        salon = Salon.objects.all()
        serializer = SalonSerializers(salon, many = True)
        return Response({'data': serializer.data})

class CreateUserView(CreateAPIView):

    permission_classes = [permissions.AllowAny]
    
    model = User
    serializer_class = UserCreateSerializers


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        users = User.objects.all()
        serializer = UserSerializers(users, many = True)

        return Response({'data': serializer.data})

class ServiceView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        service = Service.objects.all()
        serializer = ServiceSerializers(service, many = True)
        return Response({'data': serializer.data})


class ProfileView(APIView):

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


class MasterView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        master = Master.objects.all()
        serializer = MasterSerializers(master, many = True)
        return Response({'data': serializer.data})


class MasterDetailView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        master = Master.objects.get(pk=pk)
        serializer = MasterSerializers(master)
        return Response({'data': serializer.data})


class OrderView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        order = Order.objects.all()
        serializer = OrderSerializers(order, many = True)
        return Response({'data': serializer.data})

    def post(self, request):

        # if request.user.type != 2:
        #     return Response({'message': 'not allowed'})

        print(request.data)

        order = OrderPostSerializers(data = request.data)
        
        if order.is_valid():
            order.save(user = request.user)
            return Response({'status': 'added new order'})
        else:
            return Response({'status': order.errors})

class OrderDetailView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializers(order)
        return Response({'data': serializer.data})

class MastersOrderView(APIView):

    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def get(self, request):

        if request.user.type == 1:
            return Response({'error': 'You are not allowed'})

        orders = Order.objects.filter(Q(state = 1) & Q(master = request.user.master))
        serializer = OrderSerializers(orders, many = True)
        return Response({'data': serializer.data})



class ServiceAndTime(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        service = request.GET['service']

        salons = Salon.objects.filter(Q(master__service = service))

        serializer = SalonSerializers(salons, many = True)
        return Response({'data': serializer.data})


class ServiceAndSalon(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        service = request.GET['service']
        salon = request.GET['salon']

        # salons = Salon.objects.filter(Q(master__service = service))

        masters = Master.objects.filter(Q(salon__id = salon) & Q(service__id = service))

        serializer = MasterSerializers(masters, many = True)
        return Response({'data': serializer.data})

