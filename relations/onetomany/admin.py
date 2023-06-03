from django.contrib import admin
from .models import Departments,Employees
from django.contrib import admin

# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name','age','department')

admin.site.register(Departments)
admin.site.register(Employees,EmployeesAdmin)

