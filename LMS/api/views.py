from django.shortcuts import render
from django.http import JsonResponse
from teacher.models import Teacher
from student.models import Student
from .serializers import TeacherSerializer,StudentSerializer,MentorSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework import mixins,generics
from rest_framework import viewsets
from mentor.models import Mentor
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
            return Response(datas.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method=='DELETE':
        # try:
        #     teacher_data=Teacher.objects.get(id=pk)
        # except Teacher.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        teacher_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# def students_api_view(request):
#     pass
'''
class based view
class StudentViews(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data=request.data
        query_set=StudentSerializer(data=data)
        if query_set.is_valid():
            query_set.save() 
            return Response(query_set.data,status=status.HTTP_201_CREATED)
        else:
            return Response(query_set.errors,status=status.HTTP_400_BAD_REQUEST)


class StudentDetails(APIView):
    def get(self,request,pk):
        try:
            students=Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=StudentSerializer(students)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            student=Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        datas=StudentSerializer(student,data=request.data)
        if datas.is_valid():
            datas.save()
            return Response(datas.data,status=status.HTTP_200_OK)
        else:
            return Response(datas.errors,status=status.HTTP_404_NOT_FOUND) 
    def delete(self,request,pk):
        try:
            student=Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''


#mixins
'''
class StudentViews(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Student.objects.all()
    #queryset is a keyword should be queryset only
    serializer_class=StudentSerializer
    #serializer_class is a keyword
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    

class StudentDetails(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Student.objects.all()
    #queryset is a keyword should be queryset only
    serializer_class=StudentSerializer
    #serializer_class is a keyword
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
        '''
'''
class StudentViews(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    #queryset is a keyword should be queryset only
    serializer_class=StudentSerializer
    #serializer_class is a keyword
'''

'''
# class StudentDetails(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    #queryset is a keyword should be queryset only
    serializer_class=StudentSerializer
    #serializer_class is a keyword
    # lookup_field='pk'
'''


#class base view using view set 
class StudentViews(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class mentor_api(generics.ListCreateAPIView):
    queryset=Mentor.objects.all()
    serializer_class=MentorSerializer

class mentor_api_details(generics.RetrieveUpdateDestroyAPIView):
    queryset=Mentor.objects.all()
    serializer_class=MentorSerializer


   