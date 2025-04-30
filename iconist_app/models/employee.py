from django.db import models
import uuid

class Employee(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  nip = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  email = models.EmailField()
  photo = models.TextField()  # Storing base64 as text
  total_project = models.IntegerField()

  def __str__(self):
    return self.name