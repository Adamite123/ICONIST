from django.db import models
from iconist_app.models.divisi import Divisi
import uuid

class Bidang(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE, related_name='bidangs')
    nama_bidang = models.CharField(max_length=255)
    skt_bidang = models.TextField(null=True, blank=True)
