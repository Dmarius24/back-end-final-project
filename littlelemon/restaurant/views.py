from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import SingleMenuItem, Booking
from .serializers import BookingSerializer, MenuSerializer

from rest_framework.response import Response
from rest_framework import generics, viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})


class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SingleMenuItem.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = SingleMenuItem.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
