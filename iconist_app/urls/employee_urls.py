from django.urls import path
from ..views import employee_views as views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('set_bank_soal', views.set_bank_soal, name='employee_evaluation'),
    path('history', views.employee_history, name='employee_history'),
    path('history/detail', views.employee_history_detail, name='employee_history_detail'),
    path('penilaian', views.penilaian, name='employee_penilaian'),
    path('penilaian_detail', views.penilaian_detail, name='penilaian_detail'),
    # path('create/', views.employee_create, name='employee_create'),
    # path('<int:pk>/edit/', views.employee_update, name='employee_update'),
    # path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
]
