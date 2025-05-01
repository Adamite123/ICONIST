from django.db import models
import uuid

class BankSoalSurveyRekan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nip = models.CharField(max_length=50) 
    tanggal_pembuatan = models.DateField()  