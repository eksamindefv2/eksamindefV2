# Generated by Django 2.0.6 on 2018-08-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0005_auto_20180815_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='sesi',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
