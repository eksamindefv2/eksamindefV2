from django.urls import reverse
from .models import Sesi,Jadual
from urusetia.models import Zon
from persediaan.models import SubKomponen, Soalan
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
# from django.utils import timezone
from .forms import SesiForm,JadualForm
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Count, Sum, Q, Case, Value, When, IntegerField

# Create your views here.





# ---------------------------------------------------------------------------------------------------------------------------------
# Soalan - List JSON
class sesi_list_json(BaseDatatableView):
    # order_columns = ['bil','namaBahagian','editLink', 'deletelink','pk']
    order_columns = ['id','BilSesi','Tahun', 'TarikhMula', 'TarikhTamat', 'Status','editLink']

    def get_initial_queryset(self):
        # icnum = self.request.GET.get(u'icnum', '')
        # return Student.objects.filter(icnum=icnum)
        return Sesi.objects.all().order_by('BilSesi')

    def filter_queryset(self, qs):

        # Getting advanced filtering indicators for dataTables 1.10.13
        search = self.request.GET.get(u'search[value]', "")
        iSortCol_0 = self.request.GET.get(u'order[0][column]', "") # Column number 0,1,2,3,4
        sSortDir_0 = self.request.GET.get(u'order[0][dir]', "") # asc, desc
        
        # Choose which column to sort
        if iSortCol_0 == '1':
          sortcol = 'BilSesi'
        elif iSortCol_0 == '2':
           sortcol = 'BilSesi'
        else:
           sortcol = 'BilSesi'


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
          q = Q(Tahun__icontains=search)
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
                qs[i].BilSesi,
                qs[i].Tahun,
                qs[i].TarikhMula,
                qs[i].TarikhTamat,
                qs[i].JumlahSkala,
                qs[i].Status,
                qs[i].created_at,
                qs[i].id,
                reverse_lazy('sesi_edit',kwargs={'pk':qs[i].pk}),
                # reverse_lazy('urusetia_home'),
                str(qs[i].pk),
                
            ])
            # print(json_data)
        return json_data


# Sesi - Papar Senarai 
def home_sesi(request):
    return render(request, 'penilaian/sesi_json.html')     

# Sesi - Tambah
def sesi_new(request):

    if request.method == "POST":
        form = SesiForm(request.POST)
        if form.is_valid():
            sesi = form.save(commit=False)
            sesi.save()
            messages.success(request, "Sesi " + str(sesi.BilSesi) + " telah dicipta ! ")
            return redirect(reverse_lazy('sesi_home'))
    else:
        form = SesiForm()
    print(request.user)
    return render(request, 'penilaian/sesi_new.html', {'form': form}) 


# Sesi - Kemaskini
def sesi_edit(request,pk):

    sesi = get_object_or_404(Sesi, pk=pk)
    if request.method == "POST":
        form = SesiForm(request.POST,instance=sesi)
        if form.is_valid():
            sesi = form.save(commit=False)
            sesi.save()
            # return redirect('post_detail', pk=post.pk)
            messages.success(request, "Sesi " + str(sesi.BilSesi) + " telah dikemaskini! ")
            return redirect(reverse_lazy('sesi_home'))
    else:
        form = SesiForm(instance=sesi)
    
    return render(request, 'penilaian/sesi_edit.html', {'form': form})

# --------------------------------------------------------------------------------------------------------------------------------

# Jadual - List JSON
class jadual_list_json(BaseDatatableView):
    # order_columns = ['bil','namaBahagian','editLink', 'deletelink','pk']
    order_columns = ['id','BilJadual','NamaJuruAudit_id', 'Status', 'BilSesi_id','editLink']

    def get_initial_queryset(self):
        # icnum = self.request.GET.get(u'icnum', '')
        # return Student.objects.filter(icnum=icnum)
        # jad = Jadual.objects.select_related('IDZon').all() 
        return Jadual.objects.select_related('IDZon').select_related('BilSesi').select_related('NamaJuruAudit').all()
        # return Zon.objects.all().order_by('NamaZon')



    def filter_queryset(self, qs):

        # Getting advanced filtering indicators for dataTables 1.10.13
        search = self.request.GET.get(u'search[value]', "")
        iSortCol_0 = self.request.GET.get(u'order[0][column]', "") # Column number 0,1,2,3,4
        sSortDir_0 = self.request.GET.get(u'order[0][dir]', "") # asc, desc
        
        # Choose which column to sort
        if iSortCol_0 == '1':
          sortcol = 'BilJadual'
        elif iSortCol_0 == '2':
           sortcol = 'BilJadual'
        else:
           sortcol = 'BilJadual'


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
          q = Q(Tahun__icontains=search)
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
                # qs[i].NamaJuruAudit_id,
                qs[i].NamaJuruAudit.first_name,
                qs[i].BilSesi.BilSesi,
                qs[i].IDZon.NamaZon,
                qs[i].BilSesi.TarikhMula,
                qs[i].BilSesi.TarikhTamat,
                # qs[i].IDZon_id,
                qs[i].Status,
                reverse_lazy('jadual_edit',kwargs={'pk':qs[i].pk}),
                # reverse_lazy('urusetia_home'),
                str(qs[i].pk),
                
            ])
            # print(json_data)
        return json_data

# Jadual - Papar Jadual 
def home_jadual(request):
    return render(request, 'penilaian/jadual_json.html') 

# Jadual - Tambah
def jadual_new(request):

    if request.method == "POST":
        form = JadualForm(request.POST)
        if form.is_valid():
            jadual = form.save(commit=False)
            jadual.save()
            messages.success(request, "Jadual " + str(jadual.BilJadual) + " telah dicipta ! ")
            return redirect(reverse_lazy('jadual_home'))
    else:
        form = JadualForm()
    print(request.user)
    return render(request, 'penilaian/jadual_new.html', {'form': form})  


#
def jadual_edit(request,pk):

    jadual = get_object_or_404(Jadual, pk=pk)
    if request.method == "POST":
        form = JadualForm(request.POST,instance=jadual)
        if form.is_valid():
            jadual = form.save(commit=False)
            jadual.save()
            # return redirect('post_detail', pk=post.pk)
            messages.success(request, "Jadual " + str(jadual.BilJadual) + " telah dikemaskini! ")
            return redirect(reverse_lazy('jadual_home'))
    else:
        form = JadualForm(instance=jadual)
    
    return render(request, 'penilaian/jadual_edit.html', {'form': form})



# _____________________________________________________________________________________________________________________

