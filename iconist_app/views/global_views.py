from django.shortcuts import render, HttpResponse

def login(request):
    return render(request, "login.html")

def home(request):
    context = {
        'active_page': 'home',
    }
    return render(request, "home2.html", context)

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