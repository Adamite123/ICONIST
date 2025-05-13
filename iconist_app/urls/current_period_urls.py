from django.urls import path
from ..views import current_period_views as views

urlpatterns = [
  path('employee-score/', views.employee_score, name='employee_score'),
  path('mttr-performance', views.mttr_performance, name='mttr_performance')
]