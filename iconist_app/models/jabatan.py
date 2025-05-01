from django.db import models
import uuid

class Jabatan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_jabatan = models.CharField(max_length=255)
    skt_jabatan = models.TextField()
