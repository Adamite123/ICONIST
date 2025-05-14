from django.contrib import admin
from .models import Vendor, Employee, User

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Employee)
admin.site.register(User)