from django.db import models
import uuid
from iconist_app.models.employee import Employee

class BankSoal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    nama_bank_soal = models.CharField(max_length=255)
    tanggal_pembuatan = models.DateField()
