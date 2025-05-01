from django.db import models
import uuid
from iconist_app.models.employee import Employee

class IntegrasiIconapps(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tanggal = models.DateField()
    nilai_kerapian = models.DecimalField(max_digits=5, decimal_places=2)
    kehadiran = models.IntegerField()
    jks = models.IntegerField()
    jkp = models.IntegerField()
