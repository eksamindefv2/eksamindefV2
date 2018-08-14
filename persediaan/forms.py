from django import forms
from .models import Komponen,SubKomponen,Soalan,Jawapan
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineRadios


class KomponenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KomponenForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        # self.helper.layout.append(Submit('save', 'save'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout.append(Submit('submit_change', 'Hantar', css_class="btn-primary"))
        self.helper.layout.append(HTML('<a class="btn btn-primary" href={% url "komponen_home_json" %}>Kembali</a>'))



    class Meta:
        model = Komponen
        fields = ('KodKomponen', 'NamaKomponen','Status')


class SubKomponenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubKomponenForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        # self.helper.layout.append(Submit('save', 'save'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout.append(Submit('submit_change', 'Hantar', css_class="btn-primary"))
        self.helper.layout.append(HTML('<a class="btn btn-primary" href={% url "komponen_home_json" %}>Kembali</a>'))



    class Meta:
        model = SubKomponen
        fields = ('KodSubKomponen', 'NamaSubKomponen','Status')


class SoalanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SoalanForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        # self.helper.layout.append(Submit('save', 'save'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout.append(Submit('submit_change', 'Hantar', css_class="btn-primary"))
        self.helper.layout.append(HTML('<a class="btn btn-primary" href={% url "komponen_home_json" %}>Kembali</a>'))



    class Meta:
        model = Soalan
        fields = ('NoSoalan', 'Soalan','Status')
 

class JawapanForm(forms.ModelForm):
    #radio button field
    Skala = forms.ChoiceField(
        choices = (
            ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','TB')),
        widget = forms.RadioSelect,
        initial = '6',
    )
    def __init__(self, *args, **kwargs):

       
        super(JawapanForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
       

        # You can dynamically adjust your layout
        # self.helper.layout.append(Submit('save', 'save'))
        self.helper.form_class = 'form-horizontal' 
        #self.helper.layout = Layout(Field('radio_skala'))
        #self.helper.layout.append(Layout(Field('radio_skala')))
        self.helper.layout.append(Submit('submit_change', 'Hantar', css_class="btn-primary"))
        self.helper.layout.append(HTML('<a class="btn btn-primary" href={% url "soalan_list_json" %}>Kembali</a>'))
        
        

    class Meta:
        model = Jawapan
        fields = ('NoJawapan', 'DeskripsiJawapan','Skala')
 
