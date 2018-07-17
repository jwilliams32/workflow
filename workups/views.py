from django.shortcuts import render, redirect
from .models import WorkUp
from . import forms
# Create your views here.

def list_work_up(request):
    work_ups = WorkUp.objects.all
    return render(request, 'workups/list_work_up.html', {'work_ups': work_ups})



# view for one doctor
def view_work_up(request, pk=None):

    if pk:
        work_up = WorkUp.objects.get(pk=pk)

    else:
        work_up = request.work_up

    return render(request, 'workups/view_work_up.html', {'work_up': work_up})

# view to create a test
def create_work_up(request):
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

    return render(request, 'workups/create_work_up.html', context)




# view to edit a test
def edit_work_up(request):
    return render(request, 'tests/edit_test.html')