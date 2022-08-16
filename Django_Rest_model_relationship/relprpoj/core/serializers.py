from rest_framework import serializers
from .models import People, Color


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ["name"]


class ColorSerializer(serializers.ModelSerializer):
    # people = PeopleSerializer()
    people_id = serializers.SerializerMethodField()

    def get_people_id(self, obj):
        person_id=Color.objects.get(id=obj.people.id)
        return {"id":person_id.id}

    class Meta:
        model = Color
        fields = "__all__"
        depth = 1
