from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    roll=  serializers.IntegerField()
    mark= serializers.FloatField()
    
    