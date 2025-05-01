from django.db import models
from iconist_app.models.bank_soal import BankSoal
import uuid

class Kompetensi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_bank_soal = models.ForeignKey(BankSoal, on_delete=models.CASCADE)
    nama_kompetensi = models.CharField(max_length=100)
    bobot = models.DecimalField(max_digits=5, decimal_places=2)
    tanggal_buat = models.DateField()
