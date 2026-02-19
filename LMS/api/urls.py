from django.urls import path
from . import views

urlpatterns = [
         
    path('teachers/', views.teachers_api_view),
    path('teacher/<int:pk>/',views.teacher_detail),
    path('students/', views.StudentViews.as_view()),
    path('students', views.StudentViews.as_view()),
    path('student/<int:pk>/',views.StudentDetails.as_view())
]