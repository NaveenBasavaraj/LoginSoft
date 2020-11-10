from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee
# Create your views here.

def index(request):
    response = "My List of Employees Goes Here"
    return HttpResponse(response)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('first_name')
    serializer_class = EmployeeSerializer