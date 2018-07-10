from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from .forms import UserForm, ProfileForm, SignUpForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password1']
            # first_name = form.cleaned_data['']
            # last_name = form.cleaned_data['']
            #
            # user = authenticate(email=email, password=password)
            # auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

def login(request):
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            return redirect('/')
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


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('index')
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })