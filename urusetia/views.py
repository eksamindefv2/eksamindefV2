
from .models import Bahagian
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
# from django.utils import timezone
# from .forms import MessageForm, SearchForm, StudentForm
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Count, Sum, Q, Case, Value, When, IntegerField

# Create your views here.

def home(request):
	return render(request,'base.html')

def index(request):
	return render(request,'dashboard.html')

def user(request):
	return render(request,'user.html')

def home_json(request):
    return render(request, 'student/home_json.html')

def home_bahagian(request):
    return render(request, 'urusetia/bahagian_json.html')





# Student JSON list filtering
class bahagian_list_json(BaseDatatableView):
    # order_columns = ['bil','namaBahagian','editLink', 'deletelink','pk']
    order_columns = ['id','NamaBahagian','BUOrgChart','Tindakan']

    def get_initial_queryset(self):
        # icnum = self.request.GET.get(u'icnum', '')
        # return Student.objects.filter(icnum=icnum)
        return Bahagian.objects.all().order_by('BUOrgChart')

    def filter_queryset(self, qs):

        # Getting advanced filtering indicators for dataTables 1.10.13
        search = self.request.GET.get(u'search[value]', "")
        iSortCol_0 = self.request.GET.get(u'order[0][column]', "") # Column number 0,1,2,3,4
        sSortDir_0 = self.request.GET.get(u'order[0][dir]', "") # asc, desc
        
        # Choose which column to sort
        if iSortCol_0 == '1':
          sortcol = 'NamaBahagian'
        elif iSortCol_0 == '2':
           sortcol = 'BUOrgChart'
        else:
           sortcol = 'NamaBahagian'


        # Choose which sorting direction : asc or desc
        if sSortDir_0 == 'asc':
          sortdir = ''
        else:
          sortdir = '-'

        # Filtering if search value is key-in
        if search:
          # Initial Q parameter value
          qs_params = None

          # Filtering other fields
          q = Q(BUOrgChart__icontains=search)|Q(NamaBahagian__icontains=search)
          qs_params = qs_params | q if qs_params else q
   
          # Completed Q queryset
          # print qs_params
          qs = qs.filter(qs_params)
          # print 'qs :' + str(qs)
          # print 'qs :'

        # print 'sortdir + sortcol : ' + sortdir + sortcol
        return qs.order_by(sortdir + sortcol)
        # return qs

    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        # json_data = {}
        json_data = []

        for i in range(len(qs)):
            json_data.append([
                i+1,
                qs[i].NamaBahagian,
                qs[i].BUOrgChart,
                # reverse_lazy('urusetia_home'),
                # reverse_lazy('urusetia_home'),
                # str(qs[i].pk),
                
            ])
            # print(json_data)
        return json_data


	