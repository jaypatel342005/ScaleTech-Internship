from rest_framework import serializers
from .models import Employee



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


    
    def validate_salary(self,value):
        if value < 10000:
            raise serializers.ValidationError("Salary must be greater than 10000")
        return value
    
    def validate_department(self,value):
        if value not in ["IT", "HR", "Finance", "Marketing", "Sales", "Other"]:
            raise serializers.ValidationError("Invalid department")
        return value
    
    def validate(self, attrs):
        if attrs['salary'] < 10000 and attrs['department'] == "IT":
            raise serializers.ValidationError("Salary must be greater than 10000")
        return attrs
    
    def validate_age(self , value):
        if value < 18 or value > 60:
            raise serializers.ValidationError("Age must be between 18 and 60")
        return value 


    