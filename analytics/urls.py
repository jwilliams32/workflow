from django.urls import path
from . import views
from django.contrib.auth import views as auth_views






urlpatterns = [

    path('analytics/doctors', views.doctor_analytics, name='doctor_analytics'),
    # path('test/<int:pk>', views.view_test, name='view_test'),
    # path('test/<int:pk>/edit', views.edit_test, name='edit_test'),
    # # path('doctor/remove/', views.doctor_remove, name='doctor_remove'),
    # path('test/create', views.create_test, name='create_test'),
    # # path('doctor/<int:pk>/test', views.add_test, name='add_test'),


]