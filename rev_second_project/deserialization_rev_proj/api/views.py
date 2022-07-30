from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import EquipSerializer
from .models import Equipment
from django.views.decorators.csrf import csrf_exempt
import io


# Create your views here.

@csrf_exempt
def equip_get_post(request):
    if request.method == "POST":
        # fetching the json_data as string format
        json_str = request.body
        # converting the json string to byte stream format
        stream = io.BytesIO(json_str)
        # now from the stram fetching the python native data using the JSONParser
        parsed_python_data = JSONParser().parse(stream)
        # here we are printing the passed python_data to see what's coming
        print(parsed_python_data)
        # now we need to create the deserialized data using the Serializer class
        ser_obj = EquipSerializer(data=parsed_python_data)
        # here we need to validate the serialized data and using this save the data
        if ser_obj.is_valid():  # validating the data
            print(ser_obj.validated_data)  # checking which data coming as validated_data
            model_obj = ser_obj.create(validate_data=ser_obj.validated_data)
            model_obj.save()  # saving the data as complex model instance into db
            return JsonResponse({"msg": "success"})
        else:
            return JsonResponse({"msg": "something went wrong"})
    else:
        # if the request is a GET request then
        # fetching all the objects from the Equipment class
        all_equip_obj = Equipment.objects.all()
        # now we need to convert this to the serialized object
        ser_get_obj = EquipSerializer(all_equip_obj, many=True)
        # now here we are using the JSONRenderer to convert the python native to Json data
        json_data = JSONRenderer().render(data=ser_get_obj.data)
        return HttpResponse(json_data, content_type="application/json")
