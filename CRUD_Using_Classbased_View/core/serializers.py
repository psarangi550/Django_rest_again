from rest_framework import serializers
from .models import Equipment


class EquipSerializer(serializers.Serializer):
    cp_number = serializers.CharField()
    sne_id = serializers.IntegerField()
    trs_area = serializers.CharField()

    def create(self, validated_data):
        return Equipment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cp_number = validated_data.get("cp_number", instance.cp_number)
        instance.sne_id = validated_data.get("sne_id", instance.sne_id)
        instance.trs_area=validated_data.get("trs_area",instance.trs_area)
        instance.save()
        return instance