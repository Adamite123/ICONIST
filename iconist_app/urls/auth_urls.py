from django.urls import path
from ..views import auth_views as views

urlpatterns = [
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
]