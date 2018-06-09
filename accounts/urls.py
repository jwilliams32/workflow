from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    # path('', views.login, name='login'),
    path('', views.index, name='index'),
    path('login/', login, {'template_name': 'agent_app/login.html'}),
    path('register/', views.register, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),

]
