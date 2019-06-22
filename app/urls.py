from django.conf.urls import url,include
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [

    url('^add_project/$', views.add_project, name='add_project'),
    url('^delete_project/$', views.delete_project, name='delete_project'),
    url('^add_task/$', views.add_task, name='add_task'),
    url('^delete_task/$', views.delete_task, name='delete_task'),

]