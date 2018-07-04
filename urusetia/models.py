from django.db import models

# Create your models here.
class Bahagian(models.Model):


	BUOrgChart = models.CharField('Nama Bahagian',max_length=300,blank=False,null=False)


	def __str__(self):
		return self.BUOrgChart