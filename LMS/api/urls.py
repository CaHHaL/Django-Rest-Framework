from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('students',views.StudentViews)
urlpatterns = [
         
    path('teachers/', views.teachers_api_view),
    path('teacher/<int:pk>/',views.teacher_detail),
    # path('students/', views.StudentViews.as_view()),
    # path('students', views.StudentViews.as_view()),
    path('',include(router.urls)),
    # path('student/<int:pk>/',views.StudentDetails.as_view())
    path('mentors/',views.mentor_api.as_view())
    
]