from django.urls import path
from . import views
from django.contrib.auth import views as auth_views






urlpatterns = [
#
    path('workups/', views.list_workup, name='list_workup'),
    path('workup/<int:pk>', views.view_workup, name='view_workup'),
#     path('test/<int:pk>/edit', views.edit_test, name='edit_test'),
#     # path('doctor/remove/', views.doctor_remove, name='doctor_remove'),
    path('workup/create', views.create_workup, name='create_workup'),
#     # path('doctor/<int:pk>/test', views.add_test, name='add_test'),
#
#
]