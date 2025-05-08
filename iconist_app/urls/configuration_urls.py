from django.urls import path
from ..views import configuration_views as views

urlpatterns = [
    path('create-question/', views.create_question, name='create_question')
]
