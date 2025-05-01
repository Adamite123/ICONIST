import uuid
from django.db import models
from iconist_app.models.employee import Employee
from iconist_app.models.bobot_kriteria import BobotKriteria

class Pembobotan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_kriteria = models.ForeignKey(BobotKriteria, on_delete=models.CASCADE) 
    score = models.FloatField()
