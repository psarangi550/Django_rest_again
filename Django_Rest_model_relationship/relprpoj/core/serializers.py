from rest_framework import serializers
from .models import People, Color


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ["name"]
        extra_kwargs = {"name": {"required": True}}


class ColorSerializer(serializers.ModelSerializer):
    people = PeopleSerializer()
    people_age = serializers.SerializerMethodField()

    def get_people_age(self, obj):
        color_id = Color.objects.get(id=obj.people.id)
        return {"age": color_id.people.age}

    class Meta:
        model = Color
        fields = "__all__"
        # depth = 1
