from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, "login.html")

@login_required(login_url='/auth/login/')
def home(request):
    context = {
        'active_page': 'home',
    }
    return render(request, "home2.html", context)

@login_required(login_url='/auth/login/')
def dashboard_sdm(request):
    dummy_data = [
        {"sub_bidang": "PLN PBO Pelayanan PLN", "seksi": "OALPC", "status": "12/44"},
        {"sub_bidang": "PLN PBO Pelayanan PLN", "seksi": "OALPC", "status": "12/44"},
        {"sub_bidang": "PLN PBO Pelayanan PLN", "seksi": "OALPC", "status": "12/44"},
    ]
    context = {
        'active_page': 'dashboard_sdm',
        'data': dummy_data,
    }
    return render(request, "dashboard/sdm.html", context)

@login_required(login_url='/auth/login/')
def dashboard_officer(request):
    context = {
        'active_page': 'dashboard_officer',
    }
    return render(request, "dashboard/officer.html", context)

# OFFICER ROLES START

def feedback(request):
    context = {
        'active_page': 'feedback',
    }
    return render(request, "officer/feedback.html", context)

def profile(request):
    context = {
        'active_page': 'profile',
    }
    return render(request, "officer/profile.html", context)

# OFFICER ROLES END

def profil(request):
    context = {
        'active_page': 'profil',
    }
    return render(request, "profil/index.html", context)

def data_Karyawan(request):
    context = {
        'active_page': 'data_Karyawan',
    }
    return render(request, "karyawan/index.html", context)

# ======================== MASTER Karyawan START =================================
def penilaian(request):
    context = {
        'active_page': 'penilaian',
    }
    return render(request, "penilaian.html", context)

def riwayat(request):
    context = {
        'active_page': 'riwayat',
    }
    return render(request, "karyawan/master/history.html", context)

def detail_riwayat_Karyawan(request):
    context = {
        'active_page': 'detail_riwayat_Karyawan',
    }
    return render(request, "detail_riwayat_Karyawan.html", context)
# ======================== MASTER Karyawan END =================================

# ======================== PERIODE BERJALAN START =================================
def score_Karyawan(request):
    context = {
        'active_page': 'score_Karyawan',
    }
    return render(request, "score_Karyawan.html", context)
# ======================== PERIODE BERJALAN END =================================