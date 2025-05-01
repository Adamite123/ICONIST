from django.db import models
import uuid
from iconist_app.models.employee import Employee
from iconist_app.models.pembobotan import Pembobotan

class PerankinganKaryawan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_pembobotan = models.ForeignKey(Pembobotan, on_delete=models.CASCADE)
    total_score = models.DecimalField(max_digits=8, decimal_places=2) 
    rank = models.IntegerField()  
