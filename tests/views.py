from django.shortcuts import render, redirect
from .models import Test
from . import forms
# Create your views here.

def list_tests(request):
    tests = Test.objects.all
    return render(request, 'tests/list_tests.html', {'tests': tests})



# view for one doctor
def view_test(request, pk=None):

    if pk:
        test = Test.objects.get(pk=pk)

    else:
        test = request.test

    return render(request, 'tests/view_test.html', {'test': test})

# view to create a test
def create_test(request):
    if request.method == 'POST':
        form = forms.CreateTest(data=request.POST)
        if form.is_valid():
            # return instance of doctor
            instance = form.save(commit=False)

            instance = request.user
            # save to database
            instance.save()

    #       save test to db
            return redirect('/tests/')
    else:
        form = forms.CreateTest
    context = {'form': form}

    return render(request, 'tests/create_test.html', context)




# view to edit a test
def edit_test(request):
    return render(request, 'tests/edit_test.html')