from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status

class EmployeeView(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
        
    def get_object(self,id):
        try:
            return Employee.objects.get(emp_id=id)
        except Employee.DoesNotExist:
            return None
    
    def get(self,request,id):
        employee = self.get_object(id)
        if employee:
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request , id):
        employee = self.get_object(id)
        if employee:
            serializer = EmployeeSerializer(employee , data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status = status.HTTP_200_OK)
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self , request , id):
        employee = self.get_object(id)
        if employee:
            employee.delete()
            return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

        
        
