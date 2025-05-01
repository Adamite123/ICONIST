import uuid
from django.db import models
from iconist_app.models.aplikasi import Aplikasi
from iconist_app.models.employee import Employee

class PersonilAplikasi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_aplikasi = models.ForeignKey(Aplikasi, on_delete=models.CASCADE)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tanggal_pemegangan = models.DateField()
    status_personil_aplikasi = models.CharField(max_length=100)
