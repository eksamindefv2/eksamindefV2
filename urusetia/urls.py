from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='urusetia_home'),
    url(r'^index',views.index,name='index'),
    url(r'^dashboard',views.index,name='index'),
    url(r'^user',views.user,name='user'),

    url(r'^list_json/$',views.bahagian_list_json.as_view(), name="bahagian_list_json"),
    url(r'^bahagian/$',views.home_bahagian,name='bahagian_home_json'),
    url(r'^bahagian/new/$', views.bahagian_new, name='bahagian_new'),
    # url(r'^bahagian/edit/$', views.bahagian_edit, name='bahagian_edit'),
    # url(r'^(?P<pk>\d+)/edit$', views.bahagian_edit, name='bahagian_edit'),
    url(r'^bahagian/(?P<pk>\d+)/edit$', views.bahagian_edit, name='bahagian_edit'),
    url(r'^bahagian/(?P<pk>\d+)/remove$', views.bahagian_remove, name='bahagian_remove'),
    url(r'^bahagian/(?P<pk>\d+)/$', views.bahagian_detail, name='bahagian_detail'),
]