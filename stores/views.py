from django.shortcuts import render
from .serializers import PizzeriaSerializer, PizzerDetailSerializer
from rest_framework import generics
from .models import Pizzeria


class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaSerializer


class PizzerialRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()
    serializer_class = PizzerDetailSerializer

class PizzeriaDestoyAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()

class PizzeriaCreateAPIView(generics.CreateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzerDetailSerializer


class PizzeriaRetriveUpdate(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()
    serializer_class = PizzerDetailSerializer
