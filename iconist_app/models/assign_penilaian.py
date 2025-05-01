from django.db import models
from iconist_app.models.subbidang import SubBidang
from iconist_app.models.bank_soal import BankSoal
from iconist_app.models.employee import Employee
import uuid

class AssignPenilaian(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_sub_bidang = models.ForeignKey(SubBidang, on_delete=models.CASCADE)
    id_bank_soal = models.ForeignKey(BankSoal, on_delete=models.CASCADE)
    awal_periode = models.DateField()
    akhir_periode = models.DateField()
    awal_penilaian = models.DateField()
    akhir_penilaian = models.DateField()
