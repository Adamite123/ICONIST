from django.db import models
from iconist_app.models.subbidang import SubBidang
import uuid

class Seksi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_sub_bidang = models.ForeignKey(SubBidang, on_delete=models.CASCADE)
    nama_sie = models.CharField(max_length=255)
    skt_sie = models.TextField(null=True, blank=True)
