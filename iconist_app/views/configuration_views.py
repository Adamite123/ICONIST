from django.shortcuts import render

def create_question(request):
  context = {
        'active_page': 'home',
    }

  return render(request, "konfigurasi/buat_soal.html", context)

def assign_assessment(request):
  context = {
        'active_page': 'home',
    }

  return render(request, "konfigurasi/assign_assesment.html", context)
