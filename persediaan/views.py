from django.urls import reverse
from .models import Komponen,SubKomponen,Soalan,Jawapan
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
# from django.utils import timezone
from .forms import KomponenForm,SubKomponenForm, SoalanForm, JawapanForm
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Count, Sum, Q, Case, Value, When, IntegerField

# ------------------------------------------------------------------------------------------------------------------------
# Komponen -JSON List
class komponen_list_json(BaseDatatableView):
    # order_columns = ['bil','namaBahagian','editLink', 'deletelink','pk']
    order_columns = ['id','NamaKomponen','KodKomponen','Status','editLink','deletelink']

    def get_initial_queryset(self):
        # icnum = self.request.GET.get(u'icnum', '')
        # return Student.objects.filter(icnum=icnum)
        return Komponen.objects.all().order_by('KodKomponen')

    def filter_queryset(self, qs):

        # Getting advanced filtering indicators for dataTables 1.10.13
        search = self.request.GET.get(u'search[value]', "")
        iSortCol_0 = self.request.GET.get(u'order[0][column]', "") # Column number 0,1,2,3,4
        sSortDir_0 = self.request.GET.get(u'order[0][dir]', "") # asc, desc
        
        # Choose which column to sort
        if iSortCol_0 == '1':
          sortcol = 'NamaKomponen'
        elif iSortCol_0 == '2':
           sortcol = 'KodKomponen'
        else:
           sortcol = 'NamaKomponen'


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
          q = Q(NamaKomponen__icontains=search)
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
                qs[i].NamaKomponen,
                qs[i].KodKomponen,
                qs[i].Status,
                reverse_lazy('komponen_edit',kwargs={'pk':qs[i].pk}),
                reverse_lazy('komponen_remove',kwargs={'pk':qs[i].pk}),
                reverse_lazy('bahagian_detail',kwargs={'pk':qs[i].pk}),
                # reverse_lazy('urusetia_home'),
                str(qs[i].pk),
                
            ])
            # print(json_data)
        return json_data

# Komponen - Papar Senarai 
def home_komponen(request):
    return render(request, 'persediaan/komponen_json.html')

# Test views 
def jawapan_test(request):
    komponen = Komponen.objects.all()
    print(komponen)
    return render(request, 'persediaan/test.html',{'komponen': komponen})

# Tambah Komponen
def komponen_new(request):

    if request.method == "POST":
        form = KomponenForm(request.POST)
        if form.is_valid():
            komponen = form.save(commit=False)
            komponen.save()
            messages.success(request, "Komponen " + str(komponen.NamaKomponen) + " telah dicipta ! ")
            return redirect(reverse_lazy('komponen_home_json'))
    else:
        form = KomponenForm()
    print(request.user)
    return render(request, 'persediaan/komponen_new.html', {'form': form})


# Komponen - Hapus 
def komponen_remove(request,pk):

    komponen = get_object_or_404(Komponen, pk=pk)
    # if request.method == "POST":
    namaKomponen = komponen.NamaKomponen
    komponen.delete()
    messages.success(request, "Komponen : " + str(namaKomponen) + " telah dihapus! ")
    return redirect(reverse_lazy('komponen_home_json'))


# Komponen - Kemaskini 
def komponen_edit(request,pk):

    komponen = get_object_or_404(Komponen, pk=pk)
    if request.method == "POST":
        form = KomponenForm(request.POST,instance=komponen)
        if form.is_valid():
            komponen = form.save(commit=False)
            komponen.save()
            # return redirect('post_detail', pk=post.pk)
            messages.success(request, "Komponen " + str(komponen.NamaKomponen) + " telah dikemaskini! ")
            return redirect(reverse_lazy('komponen_home_json'))
    else:
        form = KomponenForm(instance=komponen)
    
    return render(request, 'persediaan/komponen_edit.html', {'form': form})


# Komponen - Details 
def komponen_detail(request,pk):

    komponen = get_object_or_404(Komponen, pk=pk)
    return render(request, 'persediaan/komponen_detail.html', {'komponen': komponen}) 


# ------------------------------------------------------------------------------------------------------------------------




# Sub Komponen - JSON List
class sub_list_json(BaseDatatableView):
    # order_columns = ['bil','namaBahagian','editLink', 'deletelink','pk']
    order_columns = ['id','KodSubKomponen','NamaSubKomponen', 'Status','editLink']

    def get_initial_queryset(self):
        Komponen_id = self.request.GET.get(u'Komponen_id', 0)
        # return Student.objects.filter(icnum=icnum)
        # return Zon.objects.all().order_by('NamaZon')
        return SubKomponen.objects.filter(Komponen_id=Komponen_id).order_by('NamaSubKomponen')

    def filter_queryset(self, qs):

        # Getting advanced filtering indicators for dataTables 1.10.13
        search = self.request.GET.get(u'search[value]', "")
        iSortCol_0 = self.request.GET.get(u'order[0][column]', "") # Column number 0,1,2,3,4
        sSortDir_0 = self.request.GET.get(u'order[0][dir]', "") # asc, desc
        
        # Choose which column to sort
        if iSortCol_0 == '1':
          sortcol = 'NamaSubKomponen'
        # elif iSortCol_0 == '2':
        #    sortcol = 'BUOrgChart'
        else:
           sortcol = 'NamaSubKomponen'


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
          q = Q(NamaSubKomponen__icontains=search)
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
                qs[i].NamaSubKomponen,
                qs[i].KodSubKomponen,
                qs[i].Status,
                reverse_lazy('subkomponen_edit',kwargs={'pk':qs[i].pk}),
                reverse_lazy('subkomponen_remove',kwargs={'pk':qs[i].pk}),
                reverse_lazy('soalan',kwargs={'pk':qs[i].pk}),
                str(qs[i].pk),
                
            ])
            # print(json_data)
        return json_data   

# Sub Komponen - Edit
def subkomponen_edit(request,pk):

    # bahagian = get_object_or_404(Bahagian, pk=pk)
    subkomponen = get_object_or_404(SubKomponen, pk=pk)
    if request.method == "POST":
        form = SubKomponenForm(request.POST,instance=subkomponen)
        if form.is_valid():
            subkomponen = form.save(commit=False)
            subkomponen.save()
            # return redirect('post_detail', pk=post.pk)
            messages.success(request, "Sub Komponen " + str(subkomponen.NamaSubKomponen) + " telah dikemaskini! ")
            return redirect(reverse_lazy('subkomponen_edit',kwargs={'pk':pk}))
    else:
        form = SubKomponenForm(instance=subkomponen)
    
    return render(request, 'persediaan/subkomponen_edit.html', {'form': form}) 


# Sub Komponen - Hapus
def subkomponen_remove(request,pk):

    subkomponen = get_object_or_404(SubKomponen, pk=pk)
    # if request.method == "POST":
    namaSubKomponen = subkomponen.NamaSubKomponen
    subkomponen.delete()
    messages.success(request, "Sub Komponen : " + str(namaSubKomponen) + " telah dihapus! ")
    return redirect(reverse_lazy('komponen_home_json'))  

# Sub Komponen - Tambah Data
def subkomponen_new(request,pk):

    # zon = get_object_or_404(Zon)
    # Bahagian_id=self.kwargs['pk']
    # print(pk)
    # Bahagian_id=pk
    if request.method == "POST":
        form = SubKomponenForm(request.POST)
        if form.is_valid():
            subkomponen = form.save(commit=False)
            subkomponen.Komponen_id = int(pk)
            subkomponen.save()
            messages.success(request, "Sub Komponen " + str(subkomponen.NamaSubKomponen) + " telah dicipta ! ")
            # return redirect(reverse_lazy('zon_new'))
            return redirect(reverse_lazy('komponen_detail',kwargs={'pk':pk}))
    else:
        form = SubKomponenForm()
    # print(request.user)
        komponen = get_object_or_404(Komponen, pk=pk)
        print(komponen)
    return render(request, 'persediaan/subkomponen_new.html', {'form': form, 'komponen': komponen} )


# ------------------------------------------------------------------------------------------------------------------------

# Soalan - Papar Soalan
def soalan(request,pk):

    subkomponen = get_object_or_404(SubKomponen, pk=pk)
    return render(request, 'persediaan/soalan_list.html', {'subkomponen': subkomponen})    



# Soalan - List JSON
class soalan_list_json(BaseDatatableView):
    # order_columns = ['bil','namaBahagian','editLink', 'deletelink','pk']
    order_columns = ['id','NoSoalan','Soalan', 'SubKomponen','editLink']

    def get_initial_queryset(self):
        SubKomponen_id = self.request.GET.get(u'SubKomponen_id', 0)
        # return Student.objects.filter(icnum=icnum)
        # return Zon.objects.all().order_by('NamaZon')
        # return Soalan.objects.all().order_by('NoSoalan')
        return Soalan.objects.filter(SubKomponen_id=SubKomponen_id).order_by('NoSoalan')

    def filter_queryset(self, qs):

        # Getting advanced filtering indicators for dataTables 1.10.13
        search = self.request.GET.get(u'search[value]', "")
        iSortCol_0 = self.request.GET.get(u'order[0][column]', "") # Column number 0,1,2,3,4
        sSortDir_0 = self.request.GET.get(u'order[0][dir]', "") # asc, desc
        
        # Choose which column to sort
        if iSortCol_0 == '1':
          sortcol = 'Soalan'
        # elif iSortCol_0 == '2':
        #    sortcol = 'BUOrgChart'
        else:
           sortcol = 'Soalan'


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
          q = Q(Soalan__icontains=search)
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
                qs[i].NoSoalan,
                qs[i].Soalan,
                # qs[i].SubKomponen_id,
                qs[i].Status,
                reverse_lazy('soalan_edit',kwargs={'pk':qs[i].pk}),
                reverse_lazy('soalan_remove',kwargs={'pk':qs[i].pk}),
                reverse_lazy('jawapan',kwargs={'pk':qs[i].pk}),
                # reverse_lazy('soalan',kwargs={'pk':qs[i].pk}),
                str(qs[i].pk),
                
            ])
            # print(json_data)
        return json_data   

 

# Soalan - Edit 
def soalan_edit(request,pk):

    soalan = get_object_or_404(Soalan, pk=pk)
    if request.method == "POST":
        form = SoalanForm(request.POST,instance=soalan)
        if form.is_valid():
            soalan = form.save(commit=False)
            soalan.save()
            # return redirect('post_detail', pk=post.pk)
            messages.success(request, "Soalan " + str(soalan.NoSoalan) + " telah dikemaskini! ")
            return redirect(reverse_lazy('soalan_edit',kwargs={'pk':pk}))
    else:
        form = SoalanForm(instance=soalan)
    
    return render(request, 'persediaan/soalan_edit.html', {'form': form}) 

# Soalan - Tambah Data
def soalan_new(request,pk):

    if request.method == "POST":
        form = SoalanForm(request.POST)
        if form.is_valid():
            soalan = form.save(commit=False)
            soalan.SubKomponen_id = int(pk)
            soalan.save()
            messages.success(request, "Soalan " + str(soalan.NoSoalan) + " telah dicipta ! ")
            # return redirect(reverse_lazy('zon_new'))
            return redirect(reverse_lazy('komponen_home_json'))
    else:
        form = SoalanForm()
    # print(request.user)
        subkomponen = get_object_or_404(SubKomponen, pk=pk)
        print(subkomponen)
    return render(request, 'persediaan/soalan_new.html', {'form': form, 'subkomponen': subkomponen} )


# Soalan - Hapus
def soalan_remove(request,pk):

    soalan = get_object_or_404(Soalan, pk=pk)
    # if request.method == "POST":
    namaSoalan = soalan.NoSoalan
    soalan.delete()
    messages.success(request, "Soalan : " + str(namaSoalan) + " telah dihapus! ")
    return redirect(reverse_lazy('komponen_home_json')) 

# ------------------------------------------------------------------------------------------------------------------------

# Jawan -- Papar Jawapan
def jawapan(request,pk):

    soalan = get_object_or_404(Soalan, pk=pk)
    return render(request, 'persediaan/jawapan_list.html', {'soalan': soalan})    



# jawapan - List JSON
class jawapan_list_json(BaseDatatableView):
    # order_columns = ['bil','namaBahagian','editLink', 'deletelink','pk']
    order_columns = ['id','NoJawapan','DeskripsiJawapan', 'Jawapan','editLink']

    def get_initial_queryset(self):
        Soalan_id = self.request.GET.get(u'Soalan_id', 0)
        # return Student.objects.filter(icnum=icnum)
        # return Zon.objects.all().order_by('NamaZon')
        # return Soalan.objects.all().order_by('NoSoalan')
        # return Jawapan.objects.all()
        return Jawapan.objects.filter(Soalan_id=Soalan_id).order_by('NoJawapan')

    def filter_queryset(self, qs):

        # Getting advanced filtering indicators for dataTables 1.10.13
        search = self.request.GET.get(u'search[value]', "")
        iSortCol_0 = self.request.GET.get(u'order[0][column]', "") # Column number 0,1,2,3,4
        sSortDir_0 = self.request.GET.get(u'order[0][dir]', "") # asc, desc
        
        # Choose which column to sort
        if iSortCol_0 == '1':
          sortcol = 'DeskripsiJawapan'
        # elif iSortCol_0 == '2':
        #    sortcol = 'BUOrgChart'
        else:
           sortcol = 'DeskripsiJawapan'


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
          q = Q(DeskripsiJawapan__icontains=search)
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
                qs[i].NoJawapan,
                qs[i].DeskripsiJawapan,
                qs[i].Skala,
                # qs[i].SubKomponen_id,
                #qs[i].Status,
                reverse_lazy('jawapan_edit',kwargs={'pk':qs[i].pk}),
                reverse_lazy('jawapan_remove',kwargs={'pk':qs[i].pk}),
                # reverse_lazy('soalan',kwargs={'pk':qs[i].pk}),
                str(qs[i].pk),
                
            ])
            # print(json_data)
        return json_data   

 
# Jawapan - Edit 
def jawapan_edit(request,pk):

    jawapan = get_object_or_404(Jawapan, pk=pk)
    if request.method == "POST":
        form = JawapanForm(request.POST,instance=jawapan)
        if form.is_valid():
            jawapan = form.save(commit=False)
            jawapan.save()
            # return redirect('post_detail', pk=post.pk)
            messages.success(request, "Jawapan " + str(jawapan.NoJawapan) + " telah dikemaskini! ")
            return redirect(reverse_lazy('jawapan_edit',kwargs={'pk':pk}))
    else:
        form = JawapanForm(instance=jawapan)
    
    return render(request, 'persediaan/jawapan_edit.html', {'form': form}) 

# Jawapan - Tambah Data
def jawapan_new(request,pk):

    if request.method == "POST":
        form = JawapanForm(request.POST)
        if form.is_valid():
            jawapan = form.save(commit=False)
            jawapan.Soalan_id = int(pk)
            jawapan.save()
            messages.success(request, "Jawapan " + str(jawapan.NoJawapan) + " telah dicipta ! ")
            # return redirect(reverse_lazy('zon_new'))
            return redirect(reverse_lazy('komponen_home_json'))
    else:
        form = JawapanForm()
    # print(request.user)
        soalan = get_object_or_404(Soalan, pk=pk)
        print(soalan)
    return render(request, 'persediaan/jawapan_new.html', {'form': form, 'soalan': soalan} )


# Jawapan - Hapus
def jawapan_remove(request,pk):

    jawapan = get_object_or_404(Jawapan, pk=pk)
    # if request.method == "POST":
    namaJawapan = jawapan.NoJawapan
    jawapan.delete()
    messages.success(request, "Jawapan : " + str(namaJawapan) + " telah dihapus! ")
    return redirect(reverse_lazy('komponen_home_json')) 