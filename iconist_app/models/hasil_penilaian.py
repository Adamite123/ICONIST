import uuid
from iconist_app.models.employee import Employee
from iconist_app.models.set_penilaian_jabatan import SetPenilaianJabatan
from django.db import models

class HasilPenilaian(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_menilai = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='hasil_penilaian_menilai')
    id_dinilai = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='hasil_penilaian_dinilai')
    id_set_penilaian_jabatan = models.ForeignKey(SetPenilaianJabatan, on_delete=models.CASCADE)
    score = models.FloatField()
    keterangan = models.TextField(blank=True, null=True)
