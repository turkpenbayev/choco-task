from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import (SalonSerializers, ServiceSerializers, UserCreateSerializers, 
        UserSerializers, ProfileSerializers, MasterSerializers, OrderSerializers, OrderPostSerializers,
        OrderCancelSerializers)

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

    # new order
    def post(self, request):

        # if request.user.type != 2:
        #     return Response({'message': 'not allowed'})


        order = OrderPostSerializers(data = request.data)
        user = request.user
        
        if order.is_valid():
            order.save(user = user)

            if user.is_verified():
                order.save(state=2)
                master = Master.objects.get(pk = order.data['master'])

                sbj = 'New order'
                msg = 'New order from user: %s'%(user)
                
                master.user.email_user(sbj, msg)
                return Response({'status': 'added new order', 'message': 'Master%s notified'%(master)})

            return Response({'status': 'added new order', 
                            'message': 'please verify phone number',
                            'link': 'http://127.0.0.1:8000/api/v1/users/verify/'})
        else:
            return Response({'status': order.errors})

    def put(self, request, format=None):

        order = OrderCancelSerializers(data = request.data)
        
        if order.is_valid():
            pk = order.data['id']
            order = get_object_or_404(Order, pk=pk)
            order.type = 3
            order.save()
            master = order.master
            sbj = 'Order canceled'
            msg = 'Order canceled from user: %s'%(request.user)
            
            master.user.email_user(sbj, msg)
            return Response({'status': 'order canceled', 'message': 'Master: %s notified'%(master)})
        else:
            return Response(order.errors)
    



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


class VerifyPhone(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({'status': request.user.is_verified()})

    def post(self, request):
        profile = request.user.profile
        code = request.POST['code']
        if code == profile.verify_code:
            profile.is_verified = True
            profile.save()
            serializer = ProfileSerializers(profile)
            return Response({'success': 'Код подтвержден', 'data': serializer.data})

        return Response({'error': 'Код не подтвержден'})