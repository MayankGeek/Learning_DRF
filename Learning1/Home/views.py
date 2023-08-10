from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse,JsonResponse
from .serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
#this view will list all the employees
#what happens in post method 
'''

so what the line of codes does is it will takes user input which will be in json then it will parse
 it and convert it into python dictionary then it will be passed to the serializer where validation 
 will be done checking if it meets all the requirements defined in the serializer and once satisfied it 
 will save it as python object and with the help of serializer.data it will display the serialized(json) 
 form of the saved data
'''
@csrf_exempt
def EmployeeListView(request):
    if request.method=="GET":
        employees = Employee.objects.all()
        serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="POST":
        #this will parse the data passed by the user
        jsonData=JSONParser().parse(request)
        # print(jsonData)
        serializer=EmployeeSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)
@csrf_exempt
def EmployeeDetailView(request,pk):
    try:
        employee=Employee.objects.get(pk=pk)
        # print(employee)
        
    except Employee.DoesNotExist:
        return HttpResponse(status=404)
        
    if request.method=="DELETE":
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    elif request.method=="GET":
        serializer=EmployeeSerializer(employee)
        # return JsonResponse("Employee"+str(pk),safe=False)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="PUT":
        jsonData=JSONParser().parse(request)
        # print(jsonData)
        serializer=EmployeeSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)
            
def UserListView(request):
    user=User.objects.all()
    serializer=UserSerializer(user,many=True)
    return JsonResponse(serializer.data,safe=False)

