from django.db import models
# from student.models import Student
# Create your models here.
class Mentor(models.Model):
    name=models.CharField(max_length=20)
    # student=models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name