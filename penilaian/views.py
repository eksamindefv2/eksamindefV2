from django.urls import reverse
from .models import Sesi
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
# from django.utils import timezone
from .forms import SesiForm
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
                qs[i].Status,
                qs[i].created_at,
                qs[i].id,
                reverse_lazy('sesi_edit',kwargs={'pk':qs[i].pk}),
                reverse_lazy('komponen_remove',kwargs={'pk':qs[i].pk}),
                reverse_lazy('bahagian_detail',kwargs={'pk':qs[i].pk}),
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

