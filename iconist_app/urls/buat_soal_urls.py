from django.urls import path
from django.contrib import admin
from ..views import buat_soal_views as views

urlpatterns = [
    path('buat_soal/', views.buat_soal, name='buat_soal')
]
