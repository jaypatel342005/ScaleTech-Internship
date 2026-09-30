from django.db import models

DEPARTMENTS = [
    ('IT', 'Information Technology'),
    ('HR', 'Human Resources'),
    ('Finance', 'Finance'),
    ('Marketing', 'Marketing'),
    ('Sales', 'Sales'),
    ('Other', 'Other'),
]

class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    salary = models.IntegerField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    department = models.CharField(max_length=10, choices=DEPARTMENTS)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name
