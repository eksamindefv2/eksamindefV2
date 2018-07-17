from django.db import models

# Create your models here.
class Bahagian(models.Model):


	BUOrgChart = models.IntegerField('BUOrgChart',unique = True,blank=False,null=False)
	NamaBahagian = models.CharField('Nama Bahagian',max_length=60,blank=False,null=False)


	def __str__(self):
		return self.BUOrgChart
		# return self.NamaBahagian


class Zon(models.Model):

	# IDZon = models.IntegerField('IDZon',unique = True,blank=False,null=False)
	NamaZon = models.CharField('NamaZon',max_length=12,blank=False,null=False)
	BUOrgChart = models.ForeignKey(Bahagian,on_delete=models.CASCADE)

	def __str__(self):
		return str (self.pk)
		# return self.NamaZon
		# return self.BUOrgChart


class Peranan(models.Model):


	ICNum = models.IntegerField('ICNum',unique = True,blank=False,null=False)
	JenisCapaian = models.CharField('JenisCapaian',max_length=60,blank=False,null=False)


	def __str__(self):
		return self.ICNum
		# return self.NamaBahagian		