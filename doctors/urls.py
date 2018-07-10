from django.urls import path
from . import views
from django.contrib.auth import views as auth_views





urlpatterns = [

    path('doctors/', views.list_doctors, name='list_doctors'),
    path('doctor/<int:pk>', views.view_doctor, name='view_doctor'),
    path('doctor/<int:pk>/edit', views.edit_doctor, name='edit_doctor'),
    # path('doctor/remove/', views.doctor_remove, name='doctor_remove'),
    path('doctor/create', views.create_doctor, name='create_doctor'),
    # path('doctor/<int:pk>/test', views.add_test, name='add_test'),


]