from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Phone(models.Model):
    phone_no = models.CharField(max_length=10)
    user_id = models.OneToOneField(User,on_delete=models.CASCADE,related_name='no')
    
    def __str__(self) :
        
        return self.phone_no
    
    