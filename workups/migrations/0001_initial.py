# Generated by Django 2.0.6 on 2018-07-25 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tests', '0001_initial'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workup_name', models.TextField(max_length=100)),
                ('workup_instruction', models.TextField(max_length=5000)),
                ('doctor', models.ManyToManyField(blank=True, related_name='workupdoctors', to='doctors.Doctor')),
                ('test', models.ManyToManyField(blank=True, related_name='workuptests', to='tests.Test')),
            ],
        ),
    ]
