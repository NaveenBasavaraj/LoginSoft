from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Employee
        fields = ('first_name','last_name','role','manager')