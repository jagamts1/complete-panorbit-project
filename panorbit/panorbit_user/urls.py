from django.conf.urls import url
from .views import index,signin,welcome,edit,logout
from django.contrib.auth import views as auth_views

app_name = 'panorbit_user'

urlpatterns = [
    url(r'^index/$',index,name="index"),
    url(r'^signin/$',signin,name="signin"),
    url(r'^welcome/$',welcome,name='welcome'),
    url(r'^edit/$',edit,name='edit'),
    url(r'^logout/$',logout,name='logout'),
	]
