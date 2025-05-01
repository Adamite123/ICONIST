from django.db import models
import uuid
from iconist_app.models.employee import Employee
from iconist_app.models.bank_soal import BankSoal
from iconist_app.models.set_penilaian_jabatan import SetPenilaianJabatan

class PenilaianSpv(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_menilai = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='penilaian_spv_menilai')
    id_dinilai = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='penilaian_spv_dinilai')
    id_bank_soal = models.ForeignKey(BankSoal, on_delete=models.CASCADE)
    id_set_penilaian_jabatan = models.ForeignKey(SetPenilaianJabatan, on_delete=models.CASCADE)
    score_total = models.DecimalField(max_digits=8, decimal_places=2)  
