from django.db import models
from iconist_app.models.bidang import Bidang
import uuid

class SubBidang(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bidang = models.ForeignKey(Bidang, on_delete=models.CASCADE)
    nama_sbi = models.CharField(max_length=255)
    skt_sbi = models.TextField(null=True, blank=True)
