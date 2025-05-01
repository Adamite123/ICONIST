import uuid
from django.db import models

class BobotKriteria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    keterangan = models.CharField(max_length=255)
    bobot = models.FloatField()
    atribut = models.CharField(max_length=255)