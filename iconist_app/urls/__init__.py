from django.urls import include, path

urlpatterns = [
    
    path('', include('iconist_app.urls.global_urls')),
    path('employees/', include('iconist_app.urls.employee_urls')),
    path('configuration/', include('iconist_app.urls.configuration_urls')),
    path('current-periode/', include('iconist_app.urls.current_period_urls')),
    path('auth/', include('iconist_app.urls.auth_urls')),
    # path('buat_soal/', include('iconist_app.urls.buat_soal_urls')),
    # path('jabatans/', include('employees.urls.jabatan_urls')),
]
