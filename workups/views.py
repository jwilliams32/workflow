from django.shortcuts import render, redirect
from .models import WorkUp
from . import forms
# Create your views here.

def list_workup(request):
    workups = WorkUp.objects.all
    return render(request, 'workups/list_workup.html', {'workups': workups})



# view for one doctor
def view_workup(request, pk=None):

    if pk:
        workup = WorkUp.objects.get(pk=pk)

    else:
        workup = request.workup

    return render(request, 'workups/view_workup.html', {'workup': workup})

# view to create a test
def create_workup(request):
    if request.method == 'POST':
        form = forms.CreateWorkUp(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            instance = request.user
            # save to database
            instance.save()

    #       save test to db
            return redirect('/tests/')
    else:
        form = forms.CreateWorkUp
    context = {'form': form}

    return render(request, 'workups/create_workup.html', context)




# view to edit a test
def edit_workup(request):
    return render(request, 'tests/edit_workup.html')