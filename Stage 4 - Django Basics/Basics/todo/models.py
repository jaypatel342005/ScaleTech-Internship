
from django.db import models

# Create your models here.
class Todo(models.Model):
    status_choices = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    ]
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20 , choices=status_choices , default='PENDING')
    priority_choices = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    priority = models.CharField(max_length=20 , choices=priority_choices , default='LOW')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



    
