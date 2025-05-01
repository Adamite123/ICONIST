from django.db import models
import uuid
from iconist_app.models.employee import Employee

class MTTR(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    score_sla = models.DecimalField(max_digits=8, decimal_places=2)  # SLA score
    score_xsla = models.DecimalField(max_digits=8, decimal_places=2)  # XSLA score
    avg_time = models.DecimalField(max_digits=8, decimal_places=2)  # Average time
    bonus_score = models.DecimalField(max_digits=8, decimal_places=2)  # Bonus score
    normal_score = models.DecimalField(max_digits=8, decimal_places=2)  # Normal score
    individual_score = models.DecimalField(max_digits=8, decimal_places=2)  # Individual score
    total_score = models.DecimalField(max_digits=8, decimal_places=2)  # Total score

    def __str__(self):
        return f"{self.nip} - {self.id_mttr}"
