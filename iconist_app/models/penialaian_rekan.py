from django.db import models
import uuid
from iconist_app.models.set_penilaian_jabatan import SetPenilaianJabatan
from iconist_app.models.soal_survey_rekan import SoalSurveyRekan
from iconist_app.models.employee import Employee

class PenilaianRekan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_set_penilaian_jabatan = models.ForeignKey(SetPenilaianJabatan, on_delete=models.CASCADE)
    id_soal_survey_rekan = models.ForeignKey(SoalSurveyRekan, on_delete=models.CASCADE)
    id_menilai = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='penilaian_rekan_menilai')
    id_dinilai = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='penilaian_rekan_dinilai')
    score_total = models.DecimalField(max_digits=8, decimal_places=2)  
