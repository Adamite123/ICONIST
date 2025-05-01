from django.db import models
import uuid
from iconist_app.models.employee import Employee
from iconist_app.models.seksi import Seksi

class HistorySie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_seksi = models.ForeignKey(Seksi, on_delete=models.CASCADE)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tanggal_join = models.DateField()
    status_personil_sie = models.CharField(max_length=50)
