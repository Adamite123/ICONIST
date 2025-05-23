# Generated by Django 5.2 on 2025-05-13 03:52

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplikasi',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_aplikasi', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('tahun_dijalankan', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BankSoalSurveyRekan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nip', models.CharField(max_length=50)),
                ('tanggal_pembuatan', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BobotKriteria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(max_length=255)),
                ('bobot', models.FloatField()),
                ('atribut', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id_vendor', models.CharField(max_length=50, unique=True)),
                ('npwp_company', models.CharField(max_length=50)),
                ('nama_company', models.CharField(max_length=100)),
                ('skt_company', models.CharField(max_length=100)),
                ('tahun_kerjasama', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Direktorat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_direktorat', models.CharField(max_length=255)),
                ('skt_direktorat', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nip', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.TextField()),
                ('total_project', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_jabatan', models.CharField(max_length=255)),
                ('skt_jabatan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='KomponenPenilaian',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('deskripsi_komponen', models.TextField()),
                ('tanggal_buat', models.DateTimeField(auto_now_add=True)),
                ('bobot_komponen', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Seksi',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_sie', models.CharField(max_length=255)),
                ('skt_sie', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('npwp', models.CharField(max_length=255)),
                ('year_of_joining', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=255)),
                ('skt', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('sdm', 'SDM'), ('spv', 'Supervisor'), ('officer', 'Officer')], max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Divisi',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_divisi', models.CharField(max_length=255)),
                ('skt_divisi', models.TextField(blank=True, null=True)),
                ('id_direktorat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisis', to='iconist_app.direktorat')),
            ],
        ),
        migrations.CreateModel(
            name='Bidang',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_bidang', models.CharField(max_length=255)),
                ('skt_bidang', models.TextField(blank=True, null=True)),
                ('id_divisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidangs', to='iconist_app.divisi')),
            ],
        ),
        migrations.CreateModel(
            name='BankSoal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_bank_soal', models.CharField(max_length=255)),
                ('tanggal_pembuatan', models.DateField()),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='AssignPenilaian',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('awal_periode', models.DateField()),
                ('akhir_periode', models.DateField()),
                ('awal_penilaian', models.DateField()),
                ('akhir_penilaian', models.DateField()),
                ('id_bank_soal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.banksoal')),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryCompany',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tgl_bergabung', models.DateField()),
                ('tgl_kontrak_berakhir', models.DateField()),
                ('status_personil_company', models.CharField(max_length=50)),
                ('id_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.company')),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='IntegrasiIconapps',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tanggal', models.DateField()),
                ('nilai_kerapian', models.DecimalField(decimal_places=2, max_digits=5)),
                ('kehadiran', models.IntegerField()),
                ('jks', models.IntegerField()),
                ('jkp', models.IntegerField()),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='IntegrasiITSM',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('jumlah_tiket_sla2', models.PositiveIntegerField(default=0)),
                ('jumlah_tiket_sla3', models.PositiveIntegerField(default=0)),
                ('jumlah_tiket_breach', models.PositiveIntegerField(default=0)),
                ('jumlah_tiket_non_sla', models.PositiveIntegerField(default=0)),
                ('rata_rata_waktu_resolved', models.FloatField()),
                ('rata_rata_peformance', models.FloatField()),
                ('tanggal', models.DateField()),
                ('id_aplikasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='integrasi_itsm', to='iconist_app.aplikasi')),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryJabatan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tanggal_awal_jabatan', models.DateField()),
                ('tanggal_akhir_jabatan', models.DateField(blank=True, null=True)),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
                ('id_jabatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.jabatan')),
            ],
        ),
        migrations.CreateModel(
            name='Kompetensi',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_kompetensi', models.CharField(max_length=100)),
                ('bobot', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tanggal_buat', models.DateField()),
                ('id_bank_soal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.banksoal')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='MTTR',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('score_sla', models.DecimalField(decimal_places=2, max_digits=8)),
                ('score_xsla', models.DecimalField(decimal_places=2, max_digits=8)),
                ('avg_time', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bonus_score', models.DecimalField(decimal_places=2, max_digits=8)),
                ('normal_score', models.DecimalField(decimal_places=2, max_digits=8)),
                ('individual_score', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_score', models.DecimalField(decimal_places=2, max_digits=8)),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Pembobotan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('score', models.FloatField()),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
                ('id_kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.bobotkriteria')),
            ],
        ),
        migrations.CreateModel(
            name='PerankinganKaryawan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_score', models.DecimalField(decimal_places=2, max_digits=8)),
                ('rank', models.IntegerField()),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
                ('id_pembobotan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.pembobotan')),
            ],
        ),
        migrations.CreateModel(
            name='PersonilAplikasi',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tanggal_pemegangan', models.DateField()),
                ('status_personil_aplikasi', models.CharField(max_length=100)),
                ('id_aplikasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.aplikasi')),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='HistorySie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tanggal_join', models.DateField()),
                ('status_personil_sie', models.CharField(max_length=50)),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
                ('id_seksi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.seksi')),
            ],
        ),
        migrations.AddField(
            model_name='aplikasi',
            name='id_seksi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.seksi'),
        ),
        migrations.CreateModel(
            name='SetPenilaianJabatan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_jabatan', models.CharField(max_length=100)),
                ('ket_otomatisasi_nilai', models.TextField(blank=True, null=True)),
                ('id_assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.assignpenilaian')),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
                ('id_komponen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.komponenpenilaian')),
            ],
        ),
        migrations.CreateModel(
            name='PenilaianSpv',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('score_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('id_bank_soal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.banksoal')),
                ('id_dinilai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penilaian_spv_dinilai', to='iconist_app.employee')),
                ('id_menilai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penilaian_spv_menilai', to='iconist_app.employee')),
                ('id_set_penilaian_jabatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.setpenilaianjabatan')),
            ],
        ),
        migrations.CreateModel(
            name='HasilPenilaian',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('score', models.FloatField()),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('id_dinilai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hasil_penilaian_dinilai', to='iconist_app.employee')),
                ('id_menilai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hasil_penilaian_menilai', to='iconist_app.employee')),
                ('id_set_penilaian_jabatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.setpenilaianjabatan')),
            ],
        ),
        migrations.CreateModel(
            name='SoalSurveyRekan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bobot', models.DecimalField(decimal_places=2, max_digits=5)),
                ('soal', models.TextField()),
                ('tanggal', models.DateField()),
                ('id_bank_soal_survey_rekan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.banksoalsurveyrekan')),
            ],
        ),
        migrations.CreateModel(
            name='PenilaianRekan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('score_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('id_dinilai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penilaian_rekan_dinilai', to='iconist_app.employee')),
                ('id_menilai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penilaian_rekan_menilai', to='iconist_app.employee')),
                ('id_set_penilaian_jabatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.setpenilaianjabatan')),
                ('id_soal_survey_rekan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.soalsurveyrekan')),
            ],
        ),
        migrations.CreateModel(
            name='StatusKaryawan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
                ('tanggal_modified', models.DateTimeField(auto_now=True)),
                ('nip_modified', models.CharField(max_length=50)),
                ('id_karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='SubBidang',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_sbi', models.CharField(max_length=255)),
                ('skt_sbi', models.TextField(blank=True, null=True)),
                ('bidang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.bidang')),
            ],
        ),
        migrations.AddField(
            model_name='seksi',
            name='id_sub_bidang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.subbidang'),
        ),
        migrations.AddField(
            model_name='assignpenilaian',
            name='id_sub_bidang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.subbidang'),
        ),
        migrations.CreateModel(
            name='SubKompetensi',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_sub', models.CharField(max_length=100)),
                ('bobot_sub', models.DecimalField(decimal_places=2, max_digits=5)),
                ('id_kompetensi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.kompetensi')),
            ],
        ),
        migrations.AddField(
            model_name='komponenpenilaian',
            name='id_sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iconist_app.subkompetensi'),
        ),
    ]
