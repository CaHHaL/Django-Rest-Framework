from django.shortcuts import render
from django.http import JsonResponse
from teacher.models import Teacher
from .serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


#serilizer and deserilizer for converting queryset to json or xml and make way other
@api_view(['GET','POST'])
def teachers_api_view(request):
    if request.method=='GET':
        teacher_datas=Teacher.objects.all()
         # teacher=list(teacher_datas.values())
        teacher_data=TeacherSerializer(teacher_datas,many=True)
        return Response(teacher_data.data)
    elif request.method=='POST':
        query_set=TeacherSerializer(data=request.data)
        if query_set.is_valid():
            query_set.save() 
            return Response(query_set.data,status=status.HTTP_201_CREATED)
        else:
            return Response(query_set.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])        
def teacher_detail(request,pk):
    try:
        teacher_data=Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        s_data=TeacherSerializer(teacher_data)
        return Response(s_data.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        data=request.data
        datas=TeacherSerializer(teacher_data,data=data)
        if datas.is_valid():
            datas.save()
            return Response(datas.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(datas.data,status=status.HTTP_404_NOT_FOUND)
    elif request.method=='DELETE':
        # try:
        #     teacher_data=Teacher.objects.get(id=pk)
        # except Teacher.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        teacher_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    