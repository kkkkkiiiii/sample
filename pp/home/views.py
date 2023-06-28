from django.shortcuts import render
from django.shortcuts import redirect
from .models import Student
from .models import POST
from .models import User


# Create your views here.

def home(request) :
    return render(request, 'home.html')



def result(request):
    name = request.POST['username']
    Student = ['bob','inu','james','tom','mike']
    
    

    if name in Student:
         return render(request,'error.html')
    else:
         return render(request, 'result.html',{'user_name':name})
          

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
