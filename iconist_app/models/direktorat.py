from django.db import models
import uuid


class Direktorat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_direktorat = models.CharField(max_length=255)
    skt_direktorat = models.TextField(null=True, blank=True)
