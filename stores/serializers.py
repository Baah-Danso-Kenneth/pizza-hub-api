from rest_framework import serializers
from .models import Pizzeria

class PizzeriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'city',
            'zip_code'
        ]