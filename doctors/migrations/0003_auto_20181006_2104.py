# Generated by Django 2.0.6 on 2018-10-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctor_doctor_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
