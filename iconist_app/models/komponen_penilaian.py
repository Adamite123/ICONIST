import uuid
from django.db import models
from iconist_app.models.sub_kompetensi import SubKompetensi

class KomponenPenilaian(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_sub = models.ForeignKey(SubKompetensi, on_delete=models.CASCADE)
    deskripsi_komponen = models.TextField()
    tanggal_buat = models.DateTimeField(auto_now_add=True)
    bobot_komponen = models.FloatField()
