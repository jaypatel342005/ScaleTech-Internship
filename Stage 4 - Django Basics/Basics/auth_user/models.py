from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Custom_User(User):
    # pass
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    
