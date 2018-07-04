from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='urusetia_home'),
    url(r'^index',views.index,name='index'),
    url(r'^dashboard',views.index,name='index'),
    url(r'^user',views.user,name='user'),

]