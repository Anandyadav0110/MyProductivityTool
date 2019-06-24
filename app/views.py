from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from .models import Project,Task

# Create your views here.

def add_project(request):
    user_name = request.session.get('user_name')
    user_obj=User.objects.get(username=user_name)
    project_name = request.GET.get('project_name')

    try:
        project_obj = Project.objects.get(project_name = project_name)
    except:
        project_obj = None

    if project_obj is  None:
        Project.objects.create(project_name = project_name,user_name=user_obj)
        message = 'created'
    else:
        message = project_name + ' is already in TODO'

    data = json.dumps(message, indent=4, sort_keys=True, default=str)
    return HttpResponse(data, content_type='application/json')

def delete_project(request):
    project_name = request.GET.get('project_name')

    try:
        project_obj = Project.objects.get(project_name = project_name)
    except:
        project_obj = None
    if project_obj is not None:
        project_obj.delete()
        message = 'deleted'
    else:
        message = project_name + ' is not found'

    data = json.dumps(message, indent=4, sort_keys=True, default=str)
    return HttpResponse(data, content_type='application/json')

def add_task(request):
    project_name = request.GET.get('project_name')
    task_desc = request.GET.get('task_desc')

    try:
        project_obj = Project.objects.get(project_name = project_name)
    except:
        project_obj = None

    try:
        task_obj = Task.objects.get(project_name=project_obj,task_desc = task_desc)
    except:
        task_obj = None

    if task_obj is  None:
        Task.objects.create(project_name = project_obj,task_desc = task_desc)
        message = 'created'
    else:
        message = task_desc + ' is already in '+ project_name

    data = json.dumps(message, indent=4, sort_keys=True, default=str)
    return HttpResponse(data, content_type='application/json')

def delete_task(request):
    project_name = request.GET.get('project_name')
    task_desc = request.GET.get('task_desc')

    try:
        project_obj = Project.objects.get(project_name=project_name)
    except:
        project_obj = None

    try:
        task_obj = Task.objects.get(project_name_id=project_obj, task_desc=task_desc)
    except:
        task_obj = None

    if task_obj is not None:
        task_obj.delete()
        message = 'deleted'
    else:
        message = task_desc + ' is not found'

    data = json.dumps(message, indent=4, sort_keys=True, default=str)
    return HttpResponse(data, content_type='application/json')
