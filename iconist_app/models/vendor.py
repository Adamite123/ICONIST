from django.db import models
import uuid

class Vendor(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  npwp = models.CharField(max_length=255)
  year_of_joining = models.CharField(max_length=4)
  name = models.CharField(max_length=255)
  skt = models.CharField(max_length=255)

  def __str__(self):
    return self.name