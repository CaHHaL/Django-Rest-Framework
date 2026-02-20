from django.db import models
from mentor.models import Mentor
# Create your models here.
class Student(models.Model):
    student_id=models.IntegerField(primary_key=True)
    branch=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mentor=models.ForeignKey(Mentor,on_delete=models.SET_NULL,null=True,related_name='students')
    def __str__(self):
        return f'{self.name}'