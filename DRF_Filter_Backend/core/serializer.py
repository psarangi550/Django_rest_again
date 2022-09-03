from rest_framework import serializers
from .models import Equipment


class EquipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields="__all__"
