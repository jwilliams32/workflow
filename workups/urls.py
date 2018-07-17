from django.urls import path
from . import views
from django.contrib.auth import views as auth_views






urlpatterns = [
#
    path('workups/', views.list_work_up, name='list_work_up'),
    path('workup/<int:pk>', views.view_work_up, name='view_work_up'),
#     path('test/<int:pk>/edit', views.edit_test, name='edit_test'),
#     # path('doctor/remove/', views.doctor_remove, name='doctor_remove'),
    path('workups/create', views.create_work_up, name='create_work_up'),
#     # path('doctor/<int:pk>/test', views.add_test, name='add_test'),
#
#
]