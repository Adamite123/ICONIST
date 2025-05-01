import uuid
from django.db import models

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_vendor = models.CharField(max_length=50, unique=True)
    npwp_company = models.CharField(max_length=50)
    nama_company = models.CharField(max_length=100)
    skt_company = models.CharField(max_length=100)
    tahun_kerjasama = models.PositiveIntegerField()