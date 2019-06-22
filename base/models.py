from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.

class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=13, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email
    class Meta:
        ordering = ['-updated_at']
