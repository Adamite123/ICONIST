from django.db import models
import uuid
from iconist_app.models.employee import Employee

class StatusKaryawan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    tanggal_modified = models.DateTimeField(auto_now=True)
    nip_modified = models.CharField(max_length=50)
