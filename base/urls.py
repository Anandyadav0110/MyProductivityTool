from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('^register/$', views.register, name='register'),
    url('^unique_user/$',views.unique_user, name='unique_user'),
    url('^logout/$',views.logout, name='logout'),
    url('^login/$', views.login, name='login'),
    url('^forgot_password/$', views.forgot_password, name='forgot_password'),
    url('^oauth/', include('social_django.urls', namespace='social')),

]