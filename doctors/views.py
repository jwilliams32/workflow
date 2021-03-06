from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor
from django.views import generic
from . import forms
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

# view for all of the doctors
def list_doctors(request):
    doctors = Doctor.objects.all
    return render(request, 'doctors/list_doctors.html', {'doctors': doctors})



# view for one doctor
def view_doctor(request, pk=None):

    if pk:
        doctor = Doctor.objects.get(pk=pk)

    else:
        doctor = request.doctor

    return render(request, 'doctors/view_doctor.html', {'doctor': doctor})

@login_required(login_url="/")

# view to create a doctor
def create_doctor(request):
    if request.method == 'POST':
        form = forms.CreateDoctor(data=request.POST)
        if form.is_valid():
            # return instance of a doctor
            instance = form.save(commit=False)
            # attach doctor
            instance.agent = request.user
            # save to database
            instance.save()

    #       save deal to db
            return redirect('/doctors/')
    else:
        form = forms.CreateDoctor()
    context = {'form': form}

    return render(request, 'doctors/create_doctor.html', context)



@login_required(login_url="/")

# view to edit a doctor
def edit_doctor(request, pk):
    if request.method == 'POST':
        edit_doctor_form = CreateDoctor
        doctor = Doctor.objects.get(pk=pk)
        form = form
    else:
        doctor = request.doctor

    return render(request, 'doctors/edit_doctor.html', {'doctor':doctor})


