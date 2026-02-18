from django.shortcuts import render
from django.http import JsonResponse
from teacher.models import Teacher
from .serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


#serilizer and deserilizer for converting queryset to json or xml and make way other
@api_view(['GET'])
def teachers_api_view(request):
    teacher_datas=Teacher.objects.all()
    # teacher=list(teacher_datas.values())
    teacher_data=TeacherSerializer(teacher_datas,many=True)
    return Response(teacher_data.data)