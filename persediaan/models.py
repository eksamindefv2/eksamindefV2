from django.db import models


class Komponen(models.Model):

	KodKomponen = models.CharField('KodKomponen',unique = True,max_length=10,blank=False,null=False)
	NamaKomponen = models.CharField('NamaKomponen',max_length=60,blank=False,null=False)
	Status = models.IntegerField('Status',blank=False,null=False, default=1)


	def __str__(self):
		return self.KodKomponen


class SubKomponen(models.Model):

	Komponen = models.ForeignKey(Komponen,on_delete=models.CASCADE)
	KodSubKomponen = models.CharField('KodSubKomponen',unique = True,max_length=10,blank=False,null=False)
	NamaSubKomponen = models.CharField('NamaSubKomponen',max_length=60,blank=False,null=False)
	Status = models.IntegerField('Statussub',blank=False,null=False, default=1)


	def __str__(self):
		return str (self.pk)


class Soalan(models.Model):

	NoSoalan = models.CharField('NoSoalan',max_length=10,blank=False,null=False)
	Soalan = models.CharField('Soalan',max_length=600,blank=False,null=False)
	SubKomponen = models.ForeignKey(SubKomponen,on_delete=models.CASCADE)
	Status = models.IntegerField('Statussoalan',blank=False,null=False, default=1)


	def __str__(self):
		return str (self.pk)		

class Jawapan(models.Model):

	NoJawapan = models.CharField('NoJawapan',unique = True,max_length=10,blank=False,null=False)
	DeskripsiJawapan = models.CharField('DeskripsiJawapan',max_length=200,blank=False,null=False)
	Pemberat = models.IntegerField('Pemberat',blank=False,null=False)
	Soalan = models.ForeignKey(Soalan,on_delete=models.CASCADE)
	TarikhKemaskini = models.DateTimeField('TarikhKemaskini',max_length=60,blank=False,null=False)

	def __str__(self):
		return str (self.pk)