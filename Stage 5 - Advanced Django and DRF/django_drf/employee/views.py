from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
from rest_framework import mixins , generics , viewsets


# # class based view for employees
# class EmployeeView(APIView):
#     def get(self,request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status = status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# class EmployeeDetail(APIView):
        
#     def get_object(self,id):
#         try:
#             return Employee.objects.get(emp_id=id)
#         except Employee.DoesNotExist:
#             return None
    
#     def get(self,request,id):
#         employee = self.get_object(id)
#         if employee:
#             serializer = EmployeeSerializer(employee)
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

#     def put(self, request , id):
#         employee = self.get_object(id)
#         if employee:
#             serializer = EmployeeSerializer(employee , data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status = status.HTTP_200_OK)
#             return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
#         return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self , request , id):
#         employee = self.get_object(id)
#         if employee:
#             employee.delete()
#             return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#         return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

        
#using mixins and generic viewset      
# class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self , request):
#         return self.list(request)
    
#     def post(self , request):
#         return self.create(request)

# class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    # queryset = Employee.objects.all()
    # serializer_class = EmployeeSerializer
    

    # def get(self , request , pk):
    #     return self.retrieve(request,pk)
    
    # def put(self , request , pk):
    #     return self.update(request,pk)
    
    # def delete(self , request , pk):
    #     return self.destroy(request,pk)


# using Generics ListCreateAPIView and RetrieveUpdateDestroyAPIView
# ListAPIView and CreateAPIView
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#RetrieveAPIView and UpdateAPIView and DestroyAPIView
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'


#using viewset and modelviewset
#viewset is like a normal class based view but it is used to perform CRUD operations on a single model
#ModelViewSet is a class based view that provides CRUD operations on a model with the help of mixins and generic viewset

#ViewSet
class EmployeeViewset(viewsets.ViewSet):
    def list(self , request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self , request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self , request,pk):
        employees = Employee.objects.get(emp_id=pk)
        serializer = EmployeeSerializer(employees)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def update(self , request , pk):
        employees = Employee.objects.get(emp_id=pk)
        serializer = EmployeeSerializer(employees , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self , request , pk):
        employees = Employee.objects.get(emp_id=pk)
        employees.delete()
        return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
#ModelViewSet
class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer