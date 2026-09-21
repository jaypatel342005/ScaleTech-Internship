from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(User):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    role = models.ForeignKey('roles.Role', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.username
    