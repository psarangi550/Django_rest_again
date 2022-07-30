from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Equipments
from .serializers import EquipSerializer
import io


# Create your views here.
@csrf_exempt
def crud_all_view(request, id=None):
    if request.method == "DELETE" and id is not None:
        equip = Equipments.objects.get(id=id)
        equip.delete()
        return JsonResponse({"msg": "data deleted Successfully"})
    if request.method == "PATCH" and id is not None:
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream_data)
        eqp_object = Equipments.objects.get(pk=id)
        ser_obj = EquipSerializer(eqp_object, data=parsed_data, partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
            return JsonResponse({"msg": "data updated Successfully"}, safe=True)
        else:
            return JsonResponse({"msg": "something  went wrong"}, safe=True)
    if request.method == "PUT" and id is not None:
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream_data)
        eqp_object = Equipments.objects.get(pk=id)
        ser_obj = EquipSerializer(eqp_object, data=parsed_data)
        if ser_obj.is_valid():
            ser_obj.save()
            return JsonResponse({"msg": "data updated Successfully"}, safe=True)
        else:
            return JsonResponse({"msg": "something  went wrong"}, safe=True)
    if request.method == "POST" and id is None:
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream_data)
        ser_obj = EquipSerializer(data=parsed_data)
        # print(ser_obj.validated_data)
        if ser_obj.is_valid():  # if valid then
            print(ser_obj.validated_data)
            ser_obj.save()  # saving the data
            return JsonResponse({"msg": "data added successfully"}, safe=True)
        else:
            return JsonResponse({"msg": "something went wrong"}, safe=True)
    else:
        if id is None:
            all_obj = Equipments.objects.all()
            # fetching all the equipments
            ser_all_data = EquipSerializer(all_obj, many=True)
            # fetching the serializer  object from that
            print(ser_all_data.data)
            # from python native data type converting to the JsonFormat
            json_data = JSONRenderer().render(data=ser_all_data.data)
            # now here we need to convert the json_data to render as below
            # return HttpResponse(json_data, content_type="application/json")
            return JsonResponse(ser_all_data.data, safe=False, json_dumps_params={"indent": 2, "sort_keys": False})
        else:
            obj = Equipments.objects.get(pk=id)
            # fetching the objects stating the pk=id
            ser_single_data = EquipSerializer(obj)
            # fetching the serialized data
            json_data = JSONRenderer().render(data=ser_single_data.data)
            # now we cen send the HttpResponse as below
            return HttpResponse(json_data, content_type="application/json")
