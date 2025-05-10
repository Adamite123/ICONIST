from django.shortcuts import render

def employee_score(request):
  # return render(request, 'current_period/employee_score.html', {'active_page': 'employee_score'})
  return render(request, 'current_period/score_karyawan.html', {'active_page': 'employee_score'})

def mttr_performance(request):
  return render(request, 'current_period/mttr_performance.html', {'active_page': 'mttr_performance'})