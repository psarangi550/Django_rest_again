from django.shortcuts import render
from django.http import request
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse,HttpResponse
from .forms import StudentForm

# Create your model instance views here.
def home(request):
    rika_user=Student.objects.get(name="rika")
    stu_ser_obj=StudentSerializer(rika_user)
    print(stu_ser_obj.data)
    json_info=JSONRenderer().render(stu_ser_obj.data)
    #here we are sending the json data using the HttpResponse function
    return HttpResponse(json_info,content_type='application/json')
    #we camn also use the JsonResponse method of the django.http module as below 
    return JsonResponse(stu_ser_obj.data)

def home_all(request):
    rika_user=Student.objects.all()
    stu_ser_all=StudentSerializer(rika_user,many=True)
    print(stu_ser_all.data)
    json_info=JSONRenderer().render(stu_ser_all.data)
    #here we are sending the json data using the HttpResponse function
    # return HttpResponse(json_info,content_type='application/json')
    #we camn also use the JsonResponse method of the django.http module as below 
    return JsonResponse({"data":stu_ser_all.data},json_dumps_params={"indent":4})

def home_dynamic_obj(request,pk):
    rika_user=Student.objects.get(id=pk)
    stu_ser_all=StudentSerializer(rika_user)
    print(stu_ser_all.data)
    json_info=JSONRenderer().render(stu_ser_all.data)
    #here we are sending the json data using the HttpResponse function
    # return HttpResponse(json_info,content_type='application/json')
    #we camn also use the JsonResponse method of the django.http module as below 
    return JsonResponse({"data":stu_ser_all.data},json_dumps_params={"indent":4})


def home_form(request):
    if request.method == 'GET':
        form=StudentForm()
        context={"form":form}
    return render(request,"core/home.html",context=context)
