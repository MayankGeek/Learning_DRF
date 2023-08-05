from rest_framework import serializers
from .models import Employee
#The task of the serializer is to convert python object into json 
# here in the serializers we do the configuration and based on that the data gets converted to json the objects
class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    email=serializers.EmailField(max_length=200)
    password=serializers.CharField(max_length=200)
    designation=serializers.CharField(max_length=200)

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    is_active = serializers.BooleanField(default=True)
    # email = serializers.EmailField(max_length=255, unique=True)
    