from django.db import models
import urusetia
import persediaan



class Sesi(models.Model):


	BilSesi = models.IntegerField('BilSesi',unique = True,blank=False,null=False)
	Tahun = models.IntegerField('Tahun',blank=False,null=False)
	TarikhMula = models.DateField('TarikhMula',max_length=60,blank=False,null=False)
	TarikhTamat = models.DateField('TarikhTamat',max_length=60,blank=False,null=False)
	Status = models.CharField('TarikhTamat',max_length=60,blank=False,null=False)
	TarikhKemaskini = models.DateTimeField('TarikhKemaskini',max_length=60,blank=False,null=False)


	def __str__(self):
		return self.BilSesi


class Jadual(models.Model):

	baru = 'Baru'
	aktif = 'Aktif'
	tamat = 'Tamat'
	disahkan = 'Disahkan'

	JADUAL_CHOICES = (
		(baru, 'Baru'),
		(aktif, 'Aktif'),
		(tamat, 'Tamat'),
		(disahkan, 'Disahkan'),
	)

	BilJadual = models.IntegerField('BilJadual',unique = True,blank=False,null=False)
	IDZon = models.ForeignKey('urusetia.Zon',on_delete=models.CASCADE)
	BilSesi = models.ForeignKey(Sesi,on_delete=models.CASCADE)
	NamaJuruAudit =  models.ForeignKey('auth.User',on_delete=models.CASCADE)
	TarikhAudit = models.DateTimeField('TarikhAudit',max_length=60,blank=False,null=False)
	Status = models.CharField('Status',max_length=60,blank=False,null=False)


	def __str__(self):
		return self.BilJadual		


class Skor(models.Model):


	BilMarkah = models.IntegerField('BilMarkah',unique = True,blank=False,null=False)
	Markah = models.IntegerField('Markah',blank=False,null=False)
	TarikhSkor = models.DateTimeField('TarikhSkor',max_length=60,blank=False,null=False)
	NoSoalan = models.ForeignKey('persediaan.Soalan',on_delete=models.CASCADE)
	NoJawapan = models.ForeignKey('persediaan.Jawapan',on_delete=models.CASCADE)
	penilai = models.ForeignKey('auth.User',on_delete=models.CASCADE,null=True)
	Catatan = models.CharField('Catatan',max_length=200,blank=False,null=False)
	KomenID = models.ForeignKey('Komen',on_delete=models.CASCADE)

	def __str__(self):
		return str (self.pk)


class Komen(models.Model):

	KomenID = models.IntegerField('KomenID',unique = True,blank=False,null=False)
	Deskripsi = models.CharField('Deskripsi',max_length=200,blank=False,null=False)
	TarikhKomen = models.DateTimeField('TarikhKomen',max_length=60,blank=False,null=False)
	createdby = models.ForeignKey('auth.User',on_delete=models.CASCADE,null=True)

































