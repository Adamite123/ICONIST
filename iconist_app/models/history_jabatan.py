from django.db import models
from iconist_app.models.jabatan import Jabatan
from iconist_app.models.employee import Employee
import uuid


class HistoryJabatan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tanggal_awal_jabatan = models.DateField()
    tanggal_akhir_jabatan = models.DateField(null=True, blank=True)
