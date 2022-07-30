from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    mark=models.FloatField()
    
    def __str__(self):
        return self.name
    
    