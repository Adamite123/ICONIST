from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from ..models import Employee
from ..forms import EmployeeForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login/')
def employee_list(request):
    query = request.GET.get('q', '')
    employee_list = Employee.objects.all()

    if query:
        employee_list = employee_list.filter(Q(name__icontains=query))

    paginator = Paginator(employee_list, 10)
    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)
    return render(request, 'karyawan/index.html', {'employees': employees, 'query': query,'active_page': 'employee_list'})

def employee_history(request):
    return render(request, 'karyawan/master/history.html', {'active_page': 'employee_history'})

def employee_history_detail(request):
    query = request.GET.get('from', '')
    return render(request, 'karyawan/master/history_detail.html', {'active_page': 'employee_history_detail', 'query': query})

def set_bank_soal(request):
    return render(request, 'karyawan/master/set_bank_soal.html', {'active_page': 'evaluation'})

def penilaian(request):
    return render(request, 'karyawan/master/penilaian.html', {'active_page': 'penilaian'})

def penilaian_detail(request):
    return render(request, 'karyawan/master/penilaian_detail.html', {'active_page': 'penilaian_detail'})


# def employee_create(request):
#     form = EmployeeForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('employee_list')
#     return render(request, 'employees/employee_form.html', {'form': form})

# def employee_update(request, pk):
#     employee = get_object_or_404(Employee, pk=pk)
#     form = EmployeeForm(request.POST or None, instance=employee)
#     if form.is_valid():
#         form.save()
#         return redirect('employee_list')
#     return render(request, 'employees/employee_form.html', {'form': form})

# def employee_delete(request, pk):
#     employee = get_object_or_404(Employee, pk=pk)
#     if request.method == 'POST':
#         employee.delete()
#         return redirect('employee_list')
#     return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})
