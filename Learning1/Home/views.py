from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse,JsonResponse
from .serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User

# Create your views here.
#this view will list all the employees
def EmployeeListView(request):
    employees = Employee.objects.all()
    serializer=EmployeeSerializer(employees,many=True)
    return JsonResponse(serializer.data,safe=False)
    
def UserListView(request):
    user=User.objects.all()
    serializer=UserSerializer(user,many=True)
    return JsonResponse(serializer.data,safe=False)

