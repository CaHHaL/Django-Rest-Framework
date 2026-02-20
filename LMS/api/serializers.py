from rest_framework import serializers
from teacher.models import Teacher
from student.models import Student
from mentor.models import Mentor

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"

class StudentSerializer(serializers.ModelSerializer):
    mentor=serializers.SlugRelatedField(slug_field="name",queryset=Mentor.objects.all())
    class Meta:
        model=Student
        fields="__all__"        

class MentorSerializer(serializers.ModelSerializer):
    students=StudentSerializer(many=True,read_only=True)
    class Meta:
        model=Mentor
        fields=['id','name','students']

