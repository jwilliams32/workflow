from django.urls import path
from . import views
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.login, name='login'),
    path('', views.index, name='index'),
    path('login/', login, {'template_name': 'registration/login.html'}),
    path('register/', views.register, name='register'),
    path('update/profile/', views.update_profile, name='update_profile'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/password_change/', auth_views.password_change, name='password_change'),
    path('accounts/change_password/done', auth_views.password_change_done, name='password_change_done'),
    path('accounts/password_reset', auth_views.password_reset, name='password_reset'),
    path('accounts/password_reset/done', auth_views.password_reset_done, name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/ ', auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('accounts/ reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
]
