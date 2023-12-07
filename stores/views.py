from django.shortcuts import render
from .serializers import PizzeriaSerializer
from rest_framework import generics
from .models import Pizzeria


class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaSerializer
