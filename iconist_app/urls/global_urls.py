from django.urls import path
from django.contrib import admin
from ..views import global_views as views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('data_Karyawan/', views.data_Karyawan, name='data_Karyawan'),

    # === MASTER Karyawan START ===
    path('penilaian/', views.penilaian, name='penilaian'),
    # path('riwayat/', views.riwayat, name='riwayat'),
    path('detail_riwayat_Karyawan/', views.detail_riwayat_Karyawan, name='detail_riwayat_Karyawan'),
    # === MASTER Karyawan END ===

    # === PERIODE BERJALAN START ===
    path('score_Karyawan/', views.score_Karyawan, name='score_Karyawan'),
    # === PERIODE BERJALAN END ===
]
