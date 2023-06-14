from django.shortcuts import render
from django.shortcuts import redirect
from .models import Student
from .models import POST
from .models import User


# Create your views here.

def home(request) :
    class_ob =Student.objects.all()
    return render(request, 'home.html')



def result(request):
    name = request.POST['username']
    Student = ['inu','james','bob']
    
    if name in Student:
        is_exist = True
    else:
        is_exist = False

    return render(request, 'result.html',{'user_name':name, 'is_exist':is_exist})


def add(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'])
        
        return redirect('home')
    return render(request,'add.html')


def create(request):
    user = User()
    user.name = request.GET['name']
    user.phone_number = request.GET['phone_number']
    user.email = request.GET['email']
    user.save()

    return redirect('/')

