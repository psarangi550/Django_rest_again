from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','roll','mark']
    
    
    class Meta:
        model = Student
        fields="__all__"
    
    
# admin.site.register(Student,StudentAdmin)