from django.urls import path
from ..views import configuration_views as views

urlpatterns = [
    path('create-question/', views.create_question, name='create_question'),
    path('assign-assessment/', views.assign_assessment, name='assign_assessment'),
    path('history/', views.history, name='configuration_history'),
    path('history/employee/', views.employee, name='configuration_employee'),
]
