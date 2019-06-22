from django.shortcuts import render
from django.contrib.auth import user_logged_out
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import random
import json


import csv
from django.core.mail import EmailMessage
from django.db.models import Sum
import datetime
import locale
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from app.models import Project,Task


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:

            request.session['user'] = user.email
            all_project = Project.objects.filter().values('project_name')

            all_task = Task.objects.filter().values('task_desc')



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
        password = request.POST['re_password']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        user = User.objects.create_user(username=user_name, password=password)
        user.save()
        UserProfile.objects.create(username=user, first_name=first_name,last_name=last_name, email=email,
                                   mobile_no=mobile_no)

        return render(request, 'base/login.html')

    return render(request, 'base/register.html')

def unique_user(request):
    user_name = request.GET.get('user_name')
    print(user_name)
    user_obj = User.objects.get(username=user_name)
    if user_obj is not None:
        message='User name already teken'
    else:
        message=''
    data = json.dumps(message, indent=4, sort_keys=True, default=str)
    return HttpResponse(data, content_type='application/json')

def logout(request):
    user = getattr(request, 'user', None)
    if hasattr(user, 'is_authenticated') and not user.is_authenticated():
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)

    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()
    return render(request, 'base/login.html')


def forgot_password(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']

        if User.objects.filter(username=user_name).exists():
            user_obj = User.objects.get(username=user_name)
            password = random.randint(1000, 9999)
            print(password)
            user_obj.set_password(password)
            user_obj.save()
            # html_content = render_to_string('base/forgot_password.html',
            #                                 {'user_mail': email, 'password': password})  # ...
            # text_content = strip_tags(html_content)
            # subject = "Erp Spotter Password Recovery "
            #
            # email = EmailMessage(settings.EMAIL_SUBJECT_PREFIX + subject, text_content, "anand@shipeasy.in",
            #                      [email])
            # email.send()
            return render(request, 'base/login.html')
        return render(request, 'base/forgot_password.html')
    return render(request, 'base/forgot_password.html')

