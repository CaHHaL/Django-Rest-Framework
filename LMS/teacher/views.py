from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Home Page")


def teacher(request):
    teacher_data=[{
        'id':1,
        'name':'john',
        'email':'john@gmail.com'
    }]
    return HttpResponse(teacher_data)