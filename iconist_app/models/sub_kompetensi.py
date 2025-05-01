import uuid
from django.db import models
from iconist_app.models.kompetensi import Kompetensi

class SubKompetensi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_kompetensi = models.ForeignKey(Kompetensi, on_delete=models.CASCADE)
    nama_sub = models.CharField(max_length=100)
    bobot_sub = models.DecimalField(max_digits=5, decimal_places=2)
