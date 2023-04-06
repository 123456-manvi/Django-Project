from django.shortcuts import render
from rest_framework import generics, status
# from django.http import HttpResponse

from .models import Room
from .serializers import RoomSerializer

# Create your views here.


class RoomView(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer



