from django.urls import include, path

urlpatterns = [
    
    path('', include('iconist_app.urls.global_urls')),
    path('employees/', include('iconist_app.urls.employee_urls')),
    # path('jabatans/', include('employees.urls.jabatan_urls')),
]
