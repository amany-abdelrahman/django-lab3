from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Student

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'lab3/signup.html')
    students = Student.objects.all()
    return render(request, 'lab3/home.html', {'students': students})

def contact(request):
    if not request.user.is_authenticated:
        return render(request, 'lab3/signup.html')
    return render(request, 'lab3/contact.html')

def about(request):
    if not request.user.is_authenticated:
        return render(request, 'lab3/signup.html')
    return render(request, 'lab3/about.html')

def student(request):
    if not request.user.is_authenticated:
        return render(request, 'lab3/signup.html')
    
    students = Student.objects.all()
    return render(request, 'lab3/home.html', {'students': students})

def create(request):
    if not request.user.is_authenticated:
        return render(request, 'lab3/signup.html')

    if request.method == 'GET':
        return render(request, 'lab3/create_student.html')

    if request.method == 'POST':
        id = request.POST['id']
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        age = request.POST['age']
        
        Student.objects.create(id=id, f_name=f_name, l_name=l_name, age=age)
        return redirect('student')

def delete_student(request, id):
    if not request.user.is_authenticated:
        return render(request, 'lab3/signup.html')
    
    Student.objects.get(id=id).delete()
    return redirect('student')

def update(request, id):
    if not request.user.is_authenticated:
        return render(request, 'lab3/signup.html')
    student = Student.objects.get(id=id)
    context = {'students': student}
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        student.f_name = fname
        student.l_name = lname
        student.age = age
        student.save()
        return redirect('student')
    return render(request, 'lab3/update_student.html', context)

def signup(request):
    if request.method == 'GET':
        return render(request, 'lab3/signup.html')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        if User.objects.filter(email=email).exists():
            context = {
                'error_message': "Email is already taken, please try again with a different email"
            }
            return render(request, 'lab3/signup.html', context)
        new_user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        login(request, new_user)
        return redirect('student')
def signin(request):
    if request.method == 'GET':
        return render(request, 'lab3/login.html')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print("Email:", email)  
        print("Password:", password) 
        User = authenticate(request, username=email, password=password)
        if User is not None:
            login(request, User)
            return redirect('student')
        else:
            print("Authentication failed!") 
            context = {'error_message': 'Invalid email or password'}
            return render(request, 'lab3/login.html', context)

def Logout(request):
    logout(request)
    return redirect('signup')
