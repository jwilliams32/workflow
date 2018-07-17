# Generated by Django 2.0.6 on 2018-07-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctors_name', models.CharField(max_length=500)),
                ('clinic_type', models.CharField(max_length=75)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
