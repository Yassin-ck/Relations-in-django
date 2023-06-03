from django.db import models

# Create your models here.

class Departments(models.Model):
    names = models.CharField(max_length=50)
    location = models.CharField(max_length=60,null=True)
    def __str__(self):
        return self.names
    
class Employees(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(Departments,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name
