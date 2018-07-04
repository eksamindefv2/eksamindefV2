from django.db import models

# Create your models here.
class Komponen(models.Model):


	KodKomponen = models.string.Primary('KodKomponen',max_length=3,blank=False,null=False)
	NamaKomponen = models.string('NamaKomponen',max_length=60,blank=False,null=False)

	def __str__(self):
		return self.Komponen

class SubKomponen(models.Model):


	KodSubKomponen = models.string.Primary('Kod Sub Komponen',max_length=3,blank=False,null=False)
	NamaSubKomponen= models.string('Nama Sub Komponen',max_length=60,blank=False,null=False)
	KodKomponen = models.string.ForeignKey('Kod Komponen',max_length=3,blank=False,null=False)

	def __str__(self):
		return self.SubKomponen

class Soalan(models.Model):


	NoSoalan = models.int.Primary('Nombor Soalan',max_length=3,blank=False,null=False)
	NamaSoalan= models.string('Nama Soalan',max_length=200,blank=False,null=False)
	KodSubKomponen = models.string.ForeignKey('Kod Sub Komponen',max_length=3,blank=False,null=False)

	def __str__(self):
		return self.SubKomponen
		

Class Soalan
{
      NoSoalan (int) 3 -Primary Key
      NamaSoalan (string) 200
      KodSubKomponen( string) 3 - Foriegn Key 
}
Class Jawapan
{
    NoJawapan  (int) 3
    DeskripsiJawapan  (string) 200
    NoSoalan (int) 3 - Foriegn Key 
    TarikhKemaskini (date)
}
