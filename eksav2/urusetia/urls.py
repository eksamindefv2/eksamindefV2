from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='urusetia_home'),
    url(r'^index',views.index,name='index'),
    url(r'^dashboard',views.index,name='index'),
    url(r'^user',views.user,name='user'),

    url(r'^list_json/$',views.bahagian_list_json.as_view(), name="bahagian_list_json"),
    url(r'^list_zon_json/$',views.zon_list_json.as_view(), name="zon_list_json"),
    url(r'^bahagian/(?P<pk>\d+)/editzon$', views.zon_edit, name='zon_edit'),
    url(r'^bahagian/(?P<pk>\d+)/removezon$', views.zon_remove, name='zon_remove'),
    # url(r'^bahagian/new_zon/$', views.zon_new, name='zon_new'),
    url(r'^bahagian/new_zon/(?P<pk>\d+)/$', views.zon_new, name='zon_new_url'),
    # url(r'^bahagian/new_zon/(?P<pk>\d+)/$', views.zon_new, name='zon_new'),
    # url(r'^bahagian/(?P<pk>\d+)/new_zon$', views.zon_new, name='zon_new'),


    url(r'^zon/$',views.zon,name='zon'),
    url(r'^dummy/$',views.dummy_view,name='dummy_url'),
 

    url(r'^bahagian/$',views.home_bahagian,name='bahagian_home_json'),
    url(r'^bahagian/new/$', views.bahagian_new, name='bahagian_new'),
    # url(r'^bahagian/edit/$', views.bahagian_edit, name='bahagian_edit'),
    # url(r'^(?P<pk>\d+)/edit$', views.bahagian_edit, name='bahagian_edit'),
    url(r'^bahagian/(?P<pk>\d+)/edit$', views.bahagian_edit, name='bahagian_edit'),
    url(r'^bahagian/(?P<pk>\d+)/remove$', views.bahagian_remove, name='bahagian_remove'),
    url(r'^bahagian/(?P<pk>\d+)/$', views.bahagian_detail, name='bahagian_detail'),
]