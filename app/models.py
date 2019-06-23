from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=30,unique=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.project_name
    class Meta:
        ordering = ['-updated_at']

class Task(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.task_desc
    class Meta:
        ordering = ['-updated_at']