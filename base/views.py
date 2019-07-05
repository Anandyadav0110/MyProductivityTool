from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import random
import json
from .models import UserProfile
from app.models import Project,Task


# Create your views here.

def login(request):
    user = request.session.get('user_name')
    if user is not None:
        all_project = Project.objects.filter().values('project_name','id')
        all_task = Task.objects.filter().values('task_desc','id')
        return render(request, 'todo.html', {'all_project': all_project, 'all_task': all_task})
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        print(username,password)

        user = authenticate(username=username, password=password)

        if user is not None:

            all_project = Project.objects.filter(user_name=user).values('project_name')

            all_task = Task.objects.filter().values('task_desc')
            request.session['user_name'] = username


            return render(request, 'todo.html', {'all_project':all_project,'all_task':all_task})
        else:
                return render(request, 'base/login.html', {"message": "Invalid Credentials"})

    else:
        return render(request, 'base/login.html')


def register(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        user = User.objects.create_user(username=user_name, password=password,email=email)
        user.save()
        UserProfile.objects.create(username=user, first_name=first_name,last_name=last_name, email=email,
                                   mobile_no=mobile_no)

        return render(request, 'base/login.html')

    return render(request, 'base/register.html')

def unique_user(request):
    user_name = request.GET.get('user_name')

    user_obj = User.objects.get(username=user_name)
    if user_obj is not None:
        message='User name already teken'
    else:
        message=''
    data = json.dumps(message, indent=4, sort_keys=True, default=str)
    return HttpResponse(data, content_type='application/json')

def logout(request):
    request.session.flush()
    return render(request, 'base/login.html')


def forgot_password(request):

    if request.method == 'POST':
        user_name = request.POST['user_name']

        if User.objects.filter(username=user_name).exists():
            user_obj = User.objects.get(username=user_name)
            password = random.randint(1000, 9999)
            print("==============New Password==================")
            print(password)
            user_obj.set_password(password)
            user_obj.save()

            # text_content = "Your new password is " + str(password) + " for user name " + user_name
            # subject = "Forgot password"
            #
            # email = EmailMessage(subject, text_content, "anandyadav0110@gmail.com",
            #                      [user_obj.email])  # emp_id['email]
            # email.send()

            return render(request, 'base/login.html')
        return render(request, 'base/forgot_password.html')
    return render(request, 'base/forgot_password.html')

