from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, SingleMenuItem

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleMenuItem
        fields = ['url', 'username', 'email', 'groups']

class SingleMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleMenuItem
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
