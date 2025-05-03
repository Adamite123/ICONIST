from django.shortcuts import render, HttpResponse

def buat_soal(request):
    context = {
        'active_page': 'home',
    }
    return render(request, "konfigurasi/buat_soal.html", context)