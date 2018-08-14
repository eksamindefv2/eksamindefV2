from django.urls import reverse
from .models import Bahagian,Zon
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
# from django.utils import timezone
from .forms import BahagianForm,ZonForm
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Count, Sum, Q, Case, Value, When, IntegerField

# Create your views here.

def dummy_view(request):

	z = Zon.objects.filter(BUOrgChart=2)
	print(z)
	return render(request,'urusetia/dummy.html',{'z': z})

def home(request):
	return render(request,'base.html')

def index(request):
	return render(request,'dashboard.html')

# Login Form
def login(request):
    return render(request,'registration/login_new.html')

def user(request):
	return render(request,'user.html')

def home_json(request):
    return render(request, 'student/home_json.html')

# Senarai Bahagian
def home_bahagian(request):
    return render(request, 'urusetia/bahagian_json.html')

# Senarai Zon
def zon(request):
    return render(request, 'urusetia/zon_json.html')


# Tambah Bahagian
def bahagian_new(request):

    if request.method == "POST":
        form = BahagianForm(request.POST)
        if form.is_valid():
            bahagian = form.save(commit=False)
            bahagian.save()
            messages.success(request, "Bahagian " + str(bahagian.NamaBahagian) + " telah dicipta ! ")
            return redirect(reverse_lazy('bahagian_home_json'))
    else:
        form = BahagianForm()
    print(request.user)
    return render(request, 'urusetia/bahagian_new.html', {'form': form})


# Tambah Zon
def zon_new(request,pk):

    # zon = get_object_or_404(Zon)
    # Bahagian_id=self.kwargs['pk']
    # print(pk)
    # Bahagian_id=pk
    if request.method == "POST":
        form = ZonForm(request.POST)
        if form.is_valid():
            zon = form.save(commit=False)
            zon.Bahagian_id = int(pk)
            zon.save()
            messages.success(request, "Zon " + str(zon.NamaZon) + " telah dicipta ! ")
            # return redirect(reverse_lazy('zon_new'))
            return redirect(reverse_lazy('bahagian_detail',kwargs={'pk':pk}))
    else:
        form = ZonForm()
    # print(request.user)
        bahagian = get_object_or_404(Bahagian, pk=pk)
        print(bahagian)
    return render(request, 'urusetia/zon_new.html', {'form': form, 'bahagian': bahagian} )

# Kemaskini Bahagian
def bahagian_edit(request,pk):

    bahagian = get_object_or_404(Bahagian, pk=pk)
    if request.method == "POST":
        form = BahagianForm(request.POST,instance=bahagian)
        if form.is_valid():
            bahagian = form.save(commit=False)
            bahagian.save()
            # return redirect('post_detail', pk=post.pk)
            messages.success(request, "Bahagian " + str(bahagian.NamaBahagian) + " telah dikemaskini! ")
            return redirect(reverse_lazy('bahagian_home_json'))
    else:
        form = BahagianForm(instance=bahagian)
    
    return render(request, 'urusetia/bahagian_edit.html', {'form': form})


# Kemaskini Bahagian
def zon_edit(request,pk):

    # bahagian = get_object_or_404(Bahagian, pk=pk)
    zon = get_object_or_404(Zon, pk=pk)
    if request.method == "POST":
        form = ZonForm(request.POST,instance=zon)
        if form.is_valid():
            zon = form.save(commit=False)
            zon.save()
            # return redirect('post_detail', pk=post.pk)
            messages.success(request, "Zon " + str(zon.NamaZon) + " telah dikemaskini! ")
            return redirect(reverse_lazy('bahagian_detail',kwargs={'pk':pk}))
    else:
        form = ZonForm(instance=zon)
    
    return render(request, 'urusetia/zon_edit.html', {'form': form}) 


# Delete Bahagian
def bahagian_remove(request,pk):

    bahagian = get_object_or_404(Bahagian, pk=pk)
    # if request.method == "POST":
    namaBahagian = bahagian.NamaBahagian
    bahagian.delete()
    messages.success(request, "Bahagian : " + str(namaBahagian) + " telah dihapus! ")
    return redirect(reverse_lazy('bahagian_home_json'))

# Bahagian Detail
def bahagian_detail(request,pk):
    bahagian = get_object_or_404(Bahagian, pk=pk)
    return render(request, 'urusetia/bahagian_detail.html', {'bahagian': bahagian})    


# Delete Zon
def zon_remove(request,pk):

    zon = get_object_or_404(Zon, pk=pk)
    # if request.method == "POST":
    namaZon = zon.NamaZon
    zon.delete()
    messages.success(request, "Zon : " + str(namaZon) + " telah dihapus! ")
    return redirect(reverse_lazy('bahagian_home_json'))       


# Bahagian JSON list filtering
class bahagian_list_json(BaseDatatableView):
    # order_columns = ['bil','namaBahagian','editLink', 'deletelink','pk']
    order_columns = ['id','NamaBahagian','BUOrgChart','editLink','deletelink']

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
          q = Q(Bahagian_id__icontains=search)|Q(NamaBahagian__icontains=search)
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
                reverse_lazy('bahagian_edit',kwargs={'pk':qs[i].pk}),
                reverse_lazy('bahagian_remove',kwargs={'pk':qs[i].pk}),
                reverse_lazy('bahagian_detail',kwargs={'pk':qs[i].pk}),
                # reverse_lazy('urusetia_home'),
                str(qs[i].pk),
                
            ])
            # print(json_data)
        return json_data


# Zon JSON list filtering
class zon_list_json(BaseDatatableView):
    # order_columns = ['bil','namaBahagian','editLink', 'deletelink','pk']
    order_columns = ['id','NamaZon','editLink']

    def get_initial_queryset(self):
        Bahagian_id = self.request.GET.get(u'Bahagian_id', 0)
        # return Student.objects.filter(icnum=icnum)
        # return Zon.objects.all().order_by('NamaZon')
        return Zon.objects.filter(Bahagian_id=Bahagian_id).order_by('NamaZon')

    def filter_queryset(self, qs):

        # Getting advanced filtering indicators for dataTables 1.10.13
        search = self.request.GET.get(u'search[value]', "")
        iSortCol_0 = self.request.GET.get(u'order[0][column]', "") # Column number 0,1,2,3,4
        sSortDir_0 = self.request.GET.get(u'order[0][dir]', "") # asc, desc
        
        # Choose which column to sort
        if iSortCol_0 == '1':
          sortcol = 'NamaZon'
        # elif iSortCol_0 == '2':
        #    sortcol = 'BUOrgChart'
        else:
           sortcol = 'NamaZon'


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
          q = Q(NamaZon__icontains=search)
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
                qs[i].NamaZon,
                # qs[i].BUOrgChart,
                reverse_lazy('zon_edit',kwargs={'pk':qs[i].pk}),
                reverse_lazy('zon_remove',kwargs={'pk':qs[i].pk}),
                # reverse_lazy('bahagian_detail',kwargs={'pk':qs[i].pk}),
                # reverse_lazy('urusetia_home'),
                str(qs[i].pk),
                
            ])
            # print(json_data)
        return json_data        


	