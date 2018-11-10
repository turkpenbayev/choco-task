from rest_framework import serializers
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import (Salon, User, Service, Profile, Master, Order)

class UserCreateSerializers(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True)
    type = serializers.IntegerField(write_only = True)

    def create(self, validate_data):
        user = User.objects.create_user(email = validate_data['email'], type = validate_data['type'])
        user.set_password(validate_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'type')


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name')



class SalonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Salon
        fields = ('id', 'name', 'address')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'type')


class ProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('name', 'last_name', 'phone')


class MasterSerializers(serializers.ModelSerializer):

    name = serializers.CharField(source = 'user.profile')
    service = ServiceSerializers(many = True)
    salon = SalonSerializers()

    class Meta:
        model = Master
        fields = ('id', 'name', 'salon', 'service', 'experience', 'rating')



class OrderSerializers(serializers.ModelSerializer):

    user = UserSerializers()

    class Meta:
        model = Order
        fields = ('id', 'user', 'master', 'create_at', 'state', 'type', 'date', 'time')


class OrderPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('master', 'date', 'time')


