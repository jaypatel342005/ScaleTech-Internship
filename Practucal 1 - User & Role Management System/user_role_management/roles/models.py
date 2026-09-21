from django.db import models

# Create your models here.
class Role(models.Model):
    roleName = models.CharField(max_length=100 , unique=True)
    accessModules = models.JSONField(default=list )
    createdAt = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True) 


    def __str__(self):
        return self.roleName
    
