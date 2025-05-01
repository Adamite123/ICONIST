from django.db import models
from iconist_app.models.employee import Employee
import uuid

class Login(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  
