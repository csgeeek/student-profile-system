from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import StudentForm
from .decorators import college_head_required
from customuser.models import College, CustomUser, Student

# Create your views here.


@login_required
@college_head_required  # <-- here!
def home(request):
    collegehead = CustomUser.objects.get(username=request.user.username)
    students = collegehead.college_head.student_college_id.all()
    context = {'students': students}
    return render(request, 'college/home.html', context=context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username)
            if user.is_college_head:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('college-head-home')
                else:
                    messages.info(request, 'Username or password is incorrect')
            else:
                messages.info(request, 'You are not a college head')
        except:
            messages.info(request, 'User not found')

    return render(request, 'college/login.html')


def logoutPage(request):
    logout(request)
    return redirect('college-head-login')


@login_required
@college_head_required
def add_student(request):
    user = CustomUser.objects.get(username=request.user.username)
    collegehead = user.college_head
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            studentInstance = form.save(commit=False)
            studentInstance.college_id = user.college_head
            studentInstance.student_college_name = collegehead.college_name
            studentInstance.save()
            return redirect('college-head-home')
    form = StudentForm()
    return render(request, 'college/student-form.html', {'form': form})


@login_required
@college_head_required
def update_student(request, pk):
    user = CustomUser.objects.get(username=request.user.username)
    student = user.college_head.student_college_id.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('college-head-home')
    return render(request, 'college/student-form.html', {'form': form})
