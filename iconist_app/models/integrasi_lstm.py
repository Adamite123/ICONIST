import uuid
from django.db import models
from iconist_app.models.employee import Employee
from iconist_app.models.aplikasi import Aplikasi

class IntegrasiITSM(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_aplikasi = models.ForeignKey(Aplikasi, on_delete=models.CASCADE, related_name='integrasi_itsm')
    jumlah_tiket_sla2 = models.PositiveIntegerField(default=0)
    jumlah_tiket_sla3 = models.PositiveIntegerField(default=0)
    jumlah_tiket_breach = models.PositiveIntegerField(default=0)
    jumlah_tiket_non_sla = models.PositiveIntegerField(default=0)
    rata_rata_waktu_resolved = models.FloatField()
    rata_rata_peformance = models.FloatField()
    tanggal = models.DateField()
