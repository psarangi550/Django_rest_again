from rest_framework import serializers
from .models import Equipment


class EquipSerializer(serializers.Serializer):
    cp_number = serializers.CharField(max_length=100)
    sne_id = serializers.IntegerField()
    sch_number = serializers.IntegerField()
    trs_area = serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Equipment.objects.create(**validate_data)
