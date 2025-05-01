from django.db import models
from iconist_app.models.direktorat import Direktorat
import uuid


class Divisi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_direktorat = models.ForeignKey(Direktorat, on_delete=models.CASCADE, related_name='divisis')
    nama_divisi = models.CharField(max_length=255)
    skt_divisi = models.TextField(null=True, blank=True)
