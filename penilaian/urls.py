from django.conf.urls import include,url
from . import views

urlpatterns = [
    
    # Sesi - List JSON
    url(r'^list_sesi_json/$',views.sesi_list_json.as_view(), name="sesi_list_json"),
    url(r'^sesi/$',views.home_sesi,name='sesi_home'),

    # Tambah Sesi
    url(r'^sesi/new/$', views.sesi_new, name='sesi_new'),

    # Kemaskini
    url(r'^sesi/(?P<pk>\d+)/edit$', views.sesi_edit, name='sesi_edit'),

    # ----------------------------------------------------------------------------------------------------

    # Jadual - List Json
    url(r'^list_jadual_json/$',views.jadual_list_json.as_view(), name="jadual_list_json"),

    url(r'^jadual/$',views.home_jadual,name='jadual_home'),

    # Tambah Jadual
    url(r'^jadual/new/$', views.jadual_new, name='jadual_new'),

    # Kemaskini Jadual
    url(r'^jadual/(?P<pk>\d+)/edit$', views.jadual_edit, name='jadual_edit'),


] 