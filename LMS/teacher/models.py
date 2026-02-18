from django.db import models

# Create your models here.
class Teacher(models.Model):
    eid=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    def __str__(self):
        return f'{self.name}'