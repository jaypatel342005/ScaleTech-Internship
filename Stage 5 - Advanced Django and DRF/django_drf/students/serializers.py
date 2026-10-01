from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, attrs):
        if attrs['stu_age'] < 18:
            raise serializers.ValidationError({'age': 'Age must be at least 18'})
        


    