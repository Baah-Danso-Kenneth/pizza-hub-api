from rest_framework import serializers
from .models import Pizzeria


class PizzeriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'city',
            'zip_code',
        ]

class PizzerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'description',
            'logo_image',
            'email',
            'active'
        ]