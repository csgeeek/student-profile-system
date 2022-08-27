from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .decorators import govt_official_required
from .forms import UserRegistrationForm, CollegeRegistrationForm
from customuser.models import CustomUser, Student, College

# ALGORITHM FOR ID GENERATION
# 1. Get the last college id from the database
# 2. Generate the next word in lexicographical order
# 3. Return the new college id
# 4. Save the new college id in the database


def generateId():
    last_id = '0000'
    try:
        last_id = College.objects.last().college_id
    except:
        last_id = '0000'
    if last_id == '0000':
        return 'AAAA'
    carry = 0
    new_id = ''
    if last_id[3] == 'Z':
        carry = 1
        new_id += 'A'
    else:
        new_id += chr(ord(last_id[3]) + 1)
    i = 2
    while i >= 0 and carry == 1:
        if last_id[i] == 'Z':
            carry = 1
            new_id += 'A'
        else:
            carry = 0
            new_id += chr(ord(last_id[i]) + 1)
        i -= 1
    while i >= 0:
        new_id += last_id[i]
        i -= 1
    return new_id[::-1]
    
# Create your views here.


@login_required
@govt_official_required  # <-- here!
def home(request):
    colleges = College.objects.all()
    return render(request, 'government/home.html', {'colleges': colleges})


@login_required
@govt_official_required  # <-- here!
def viewStudentsListByCollege(request, college_id):
    college = College.objects.get(college_id=college_id)
    students = Student.objects.filter(college_id=college.id)
    context = {'students': students, 'college_id': college_id}
    return render(request, 'government/view-students-list.html', context=context)



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username)
            if user.is_govt_official:
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('govt-official-home')
                else:
                    messages.info(request, 'Username or password is incorrect')
            else:
                messages.info(request, 'You are not a govt official')
        except:
            messages.info(request, 'User not found')

    return render(request, 'government/login.html')


def logoutPage(request):
    logout(request)
    return redirect('govt-official-login')


def registerGovtOfficialPage(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_govt_official = True
            user.save()
            login(request, user)
            return redirect('govt-official-home')

    return render(request, 'government/register.html', {'form': form})


@login_required
@govt_official_required  # <-- here!
def registerCollegeAndHead(request):
    cid = generateId()
    form1 = UserRegistrationForm()
    form2 = CollegeRegistrationForm()

    context = {'form1': form1, 'form2': form2, 'collegeID': cid}
    if request.method == 'POST':
        post1 = request.POST.copy()
        post2 = request.POST.copy()
        post1.pop('college_name')
        post2.pop('username')
        post2.pop('first_name')
        post2.pop('last_name')
        post2.pop('password1')
        post2.pop('password2')
        form1 = UserRegistrationForm(post1)
        form2 = CollegeRegistrationForm(post2)
        if form1.is_valid(): # <-- here!
            userInstance = form1.save(commit=False)
            # college head registered succesfully
            userInstance.is_college_head = True
            userInstance.save()
            collegehead = CustomUser.objects.get(username=userInstance.username)
            college = form2.save(commit=False)
            college.college_head = collegehead
            college.college_id = cid

            if form2.is_valid():
                college.save()
                return redirect('govt-official-home')
            else:
                messages.info(request, 'College not registered')
        else:
            messages.info(request, 'College head not registered')

    return render(request, 'government/register-college-and-head.html', context=context)