# Generated by Django 2.0.6 on 2018-09-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persediaan', '0011_remove_jawapan_tarikhkemaskini'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jawapan',
            name='NoJawapan',
            field=models.CharField(max_length=10, verbose_name='NoJawapan'),
        ),
    ]
