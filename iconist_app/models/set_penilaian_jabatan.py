import uuid
from django.db import models
from iconist_app.models.employee import Employee
from iconist_app.models.assign_penilaian import AssignPenilaian
from iconist_app.models.komponen_penilaian import KomponenPenilaian

class SetPenilaianJabatan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_assign = models.ForeignKey(AssignPenilaian, on_delete=models.CASCADE)
    id_karyawan = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_komponen = models.ForeignKey(KomponenPenilaian, on_delete=models.CASCADE)
    nama_jabatan = models.CharField(max_length=100)
    ket_otomatisasi_nilai = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nama_jabatan} - {self.nip}"
