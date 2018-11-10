from rest_framework import serializers
from .models import Salon, User

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


class SalonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = ('id', 'name', 'address')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'type')