from django.conf.urls import include,url
from . import views

urlpatterns = [
    
    # Papar senarai Komponen
    url(r'^list_json/$',views.komponen_list_json.as_view(), name="komponen_list_json"),
    url(r'^komponen/$',views.home_komponen,name='komponen_home_json'),
    url(r'^komponen/new/$', views.komponen_new, name='komponen_new'),

    # Hapus Komponen
    url(r'^komponen/(?P<pk>\d+)/remove$', views.komponen_remove, name='komponen_remove'),

    # Edit Komponen
    url(r'^komponen/(?P<pk>\d+)/edit$', views.komponen_edit, name='komponen_edit'),
    
    # Details Komponen
    url(r'^komponen/(?P<pk>\d+)/$', views.komponen_detail, name='komponen_detail'),

    # Sub Komponen - JSON List
    url(r'^list_sub_json/$',views.sub_list_json.as_view(), name="sub_list_json"),

    # Sub Komponen - Edit
    url(r'^komponen/(?P<pk>\d+)/editsub$', views.subkomponen_edit, name='subkomponen_edit'),

    # Sub Komponen - Hapus
    url(r'^komponen/(?P<pk>\d+)/removesub$', views.subkomponen_remove, name='subkomponen_remove'),

    # Sub Komponen - Tambah Data
    url(r'^komponen/new_zon/(?P<pk>\d+)/$', views.subkomponen_new, name='subkomponen_new_url'),







]   