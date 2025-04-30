from django.urls import path
from ..views import employee_views as views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    # path('create/', views.employee_create, name='employee_create'),
    # path('<int:pk>/edit/', views.employee_update, name='employee_update'),
    # path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
]
