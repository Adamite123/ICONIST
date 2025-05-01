from django.db import models
import uuid
from iconist_app.models.bank_soal_survey_rekan import BankSoalSurveyRekan

class SoalSurveyRekan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_bank_soal_survey_rekan = models.ForeignKey(BankSoalSurveyRekan, on_delete=models.CASCADE)
    bobot = models.DecimalField(max_digits=5, decimal_places=2)  
    soal = models.TextField()  
    tanggal = models.DateField()
