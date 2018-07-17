from django.db import models


class Komponen(models.Model):

	KodKomponen = models.CharField('KodKomponen',unique = True,max_length=10,blank=False,null=False)
	NamaKomponen = models.CharField('NamaKomponen',max_length=60,blank=False,null=False)

	def __str__(self):
		return self.KodKomponen


class SubKomponen(models.Model):

	KodSubKomponen = models.CharField('KodSubKomponen',unique = True,max_length=10,blank=False,null=False)
	NamaSubKomponen = models.CharField('NamaSubKomponen',max_length=60,blank=False,null=False)
	KodKomponen = models.ForeignKey(Komponen,on_delete=models.CASCADE)

	def __str__(self):
		return str (self.pk)


class Soalan(models.Model):

	NoSoalan = models.CharField('NoSoalan',unique = True,max_length=10,blank=False,null=False)
	Soalan = models.CharField('NamaSubKomponen',max_length=200,blank=False,null=False)
	KodSubKomponen = models.ForeignKey(SubKomponen,on_delete=models.CASCADE)

	def __str__(self):
		return str (self.pk)		

class Jawapan(models.Model):

	NoJawapan = models.CharField('NoJawapan',unique = True,max_length=10,blank=False,null=False)
	DeskripsiJawapan = models.CharField('DeskripsiJawapan',max_length=200,blank=False,null=False)
	Pemberat = models.IntegerField('Pemberat',blank=False,null=False)
	NoSoalan = models.ForeignKey(Soalan,on_delete=models.CASCADE)
	TarikhKemaskini = models.DateTimeField('TarikhKemaskini',max_length=60,blank=False,null=False)

	def __str__(self):
		return str (self.pk)