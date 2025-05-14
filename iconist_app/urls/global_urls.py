from django.urls import path
from django.contrib import admin
from ..views import global_views as views
from ..views import auth_views as auth_views

urlpatterns = [
    path('', auth_views.login_view, name='login'),
    path('dashboard', views.home, name='home'),
    path('dash-sdm', views.dashboard_sdm, name='dashboard_sdm'),
    path('dash-officer', views.dashboard_officer, name='dashboard_officer'),
<<<<<<< HEAD
=======
    path('feedback', views.feedback, name='feedback'),
    path('profil', views.profil, name='profil'),
>>>>>>> 2df92bd318801a5911b7d586e7f56abac41a2f0a
    path('admin/', admin.site.urls),
    path('data_Karyawan/', views.data_Karyawan, name='data_Karyawan'),

    # === MASTER Karyawan START (SPV) ===
    path('penilaian/', views.penilaian, name='penilaian'),
    # path('riwayat/', views.riwayat, name='riwayat'),
    path('detail_riwayat_Karyawan/', views.detail_riwayat_Karyawan, name='detail_riwayat_Karyawan'),
    # === MASTER Karyawan END ===

    # === PERIODE BERJALAN START(SPV) ===
    path('score_Karyawan/', views.score_Karyawan, name='score_Karyawan'),
    # === PERIODE BERJALAN END ===

    # Profile (OFFICER)
    path('profile', views.profile, name='profile'),
    path('feedback', views.feedback, name='feedback'),
]
