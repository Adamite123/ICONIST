from django.shortcuts import render

def create_question(request):
  context = {
        'active_page': 'configuration-create-question',
    }

  return render(request, "konfigurasi/buat_soal.html", context)

def assign_assessment(request):
  context = {
        'active_page': 'configuration-assign-assessment',
    }

  return render(request, "konfigurasi/assign_assesment.html", context)

def history(request):
  dummy_data = [
    {"name": "Seksi A", "total": 10, "progress": "44/44", "status": "In Progress",},
    {"name": "Seksi B", "total": 15, "progress": "44/44", "status": "In Progress",},
    {"name": "Seksi C", "total": 20, "progress": "44/44", "status": "Completed",},
    {"name": "Seksi C", "total": 20, "progress": "44/44", "status": "Not Yet",},
  ]

  context = {
    'active_page': 'configuration-history',
    'data': dummy_data,
  }

  return render(request, "konfigurasi/history/index.html", context)

def employee(request):
  dummy_data = [
      {"no": 1, "nama_karyawan": "John Doe", "jabatan": "Manager", "vendor": "Vendor A", "sub_bidang": "IT", "aplikasi": "App X", "skor": 85},
      {"no": 2, "nama_karyawan": "Jane Smith", "jabatan": "Developer", "vendor": "Vendor B", "sub_bidang": "Software", "aplikasi": "App Y", "skor": 90},
      {"no": 3, "nama_karyawan": "Alice Johnson", "jabatan": "Analyst", "vendor": "Vendor C", "sub_bidang": "Finance", "aplikasi": "App Z", "skor": 88},
  ]

  context = {
      'active_page': 'configuration-employee',
      'data': dummy_data,
  }

  return render(request, "konfigurasi/history/employee.html", context)