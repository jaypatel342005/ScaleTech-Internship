from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.IntegerField()
    stu_name = models.CharField(max_length=20)
    stu_age = models.IntegerField()
    stu_class = models.CharField(max_length=20)
    stu_email = models.EmailField()
    stu_DOB = models.DateField()
    stu_address = models.CharField(max_length=20)
    stu_gender = models.CharField(max_length=20)
    stu_grade = models.CharField(max_length=20)
    stu_status = models.CharField(max_length=20)
    stu_created_at = models.DateTimeField(auto_now_add=True)
    stu_updated_at = models.DateTimeField(auto_now=True)
    
    #str 
    def __str__(self):
        return self.stu_name
    
    
