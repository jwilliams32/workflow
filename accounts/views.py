from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, get_user_model, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['']
            last_name = form.cleaned_data['']

            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

def login(request):
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            return redirect('index')
    else:
        form = AuthenticationForm()
    #
    # template = 'login.html'
    # context = {}
    # # return HttpResponse("Login")

    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'registration/logout.html')