import uuid
from django.db import models
from iconist_app.models.seksi import Seksi

class Aplikasi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_seksi = models.ForeignKey(Seksi, on_delete=models.CASCADE)
    nama_aplikasi = models.CharField(max_length=255)
    deskripsi = models.TextField()
    tahun_dijalankan = models.PositiveIntegerField()
