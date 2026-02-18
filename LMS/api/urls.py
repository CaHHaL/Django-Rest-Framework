from django.urls import path
from . import views

urlpatterns = [
         
    path('teachers/', views.teachers_api_view),
]
