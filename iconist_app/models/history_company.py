from django.db import models
from iconist_app.models.company import Company
from iconist_app.models.employee import Employee
import uuid

class HistoryCompany(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tgl_bergabung = models.DateField()
    tgl_kontrak_berakhir = models.DateField()
    status_personil_company = models.CharField(max_length=50)
