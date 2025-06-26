from django.db import models

class AccountType(models.Model):
    account_type_id = models.AutoField(primary_key=True)
    admin = models.BooleanField()
    peso = models.BooleanField()
    user = models.BooleanField()
    coordinator = models.BooleanField()

class Aacup(models.Model):
    aacup_id = models.AutoField(primary_key=True)
    standard = models.ForeignKey('Standard', on_delete=models.CASCADE, related_name='aacups')

class Ched(models.Model):
    ched_id = models.AutoField(primary_key=True)
    standard = models.ForeignKey('Standard', on_delete=models.CASCADE, related_name='cheds')


class CompTechJob(models.Model):
    comp_tech_jobs_id = models.AutoField(primary_key=True)
    suc = models.ForeignKey('Suc', on_delete=models.CASCADE, related_name='comptechjob_sucs')
    info_system_jobs = models.ForeignKey('InfoSystemJob', on_delete=models.CASCADE, related_name='comptechjob_infosystemjobs')
    info_tech_jobs = models.ForeignKey('InfoTechJob', on_delete=models.CASCADE, related_name='comptechjob_infotechjobs')
    job_title = models.CharField(max_length=255)

class ExportedFile(models.Model):
    exported_file_id = models.AutoField(primary_key=True)
    standard = models.ForeignKey('Standard', on_delete=models.CASCADE, related_name='exported_files')
    file_name = models.CharField(max_length=255)
    exported_date = models.DateTimeField()

class HighPosition(models.Model):
    high_position_id = models.AutoField(primary_key=True)
    aacup = models.ForeignKey('Aacup', on_delete=models.CASCADE, related_name='high_positions')
    tracker_form = models.ForeignKey('TrackerForm', on_delete=models.CASCADE, related_name='high_positions')

class Import(models.Model):
    import_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='imports')
    import_year = models.IntegerField()
    import_by = models.CharField(max_length=255)

class InfoTechJob(models.Model):
    info_tech_jobs_id = models.AutoField(primary_key=True)
    suc = models.ForeignKey('Suc', on_delete=models.CASCADE, related_name='infotechjob_sucs')
    info_systems_jobs = models.ForeignKey('InfoSystemJob', on_delete=models.CASCADE, related_name='infotechjob_infosystemjobs')
    comp_tech_jobs = models.ForeignKey('CompTechJob', on_delete=models.CASCADE, related_name='infotechjob_comptechjobs')
    job_title = models.CharField(max_length=255)

class InfoSystemJob(models.Model):
    info_system_jobs_id = models.AutoField(primary_key=True)
    suc = models.ForeignKey('Suc', on_delete=models.CASCADE, related_name='infosystemjob_sucs')
    info_tech_jobs = models.ForeignKey('InfoTechJob', on_delete=models.CASCADE, related_name='infosystemjob_infotechjobs')
    comp_tech_jobs = models.ForeignKey('CompTechJob', on_delete=models.CASCADE, related_name='infosystemjob_comptechjobs')
    job_title = models.CharField(max_length=255)

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='notifications')
    notif_type = models.CharField(max_length=100)
    notifi_content = models.TextField()
    notif_date = models.DateTimeField()

class Qpro(models.Model):
    qpro_id = models.AutoField(primary_key=True)
    standard = models.ForeignKey('Standard', on_delete=models.CASCADE, related_name='qpros')

class Standard(models.Model):
    standard_id = models.AutoField(primary_key=True)
    tracker_form = models.ForeignKey('TrackerForm', on_delete=models.CASCADE, related_name='standards')
    qpro = models.ForeignKey('Qpro', on_delete=models.CASCADE, related_name='standards')
    suc = models.ForeignKey('Suc', on_delete=models.CASCADE, related_name='standards')
    aacup = models.ForeignKey('Aacup', on_delete=models.CASCADE, related_name='standards')
    ched = models.ForeignKey('Ched', on_delete=models.CASCADE, related_name='standards')

class Suc(models.Model):
    suc_id = models.AutoField(primary_key=True)
    standard = models.ForeignKey('Standard', on_delete=models.CASCADE, related_name='suc_sucs')
    info_tech_jobs = models.ForeignKey('InfoTechJob', on_delete=models.CASCADE, related_name='suc_infotechjobs')
    info_system_jobs = models.ForeignKey('InfoSystemJob', on_delete=models.CASCADE, related_name='suc_infosystemjobs')
    comp_tech_jobs = models.ForeignKey('CompTechJob', on_delete=models.CASCADE, related_name='suc_comptechjobs')

class TrackerForm(models.Model):
    tracker_form_id = models.AutoField(primary_key=True)
    standard = models.ForeignKey('Standard', on_delete=models.CASCADE, related_name='tracker_forms')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tracker_forms')

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    import_id = models.ForeignKey('Import', on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    account_type = models.ForeignKey('AccountType', on_delete=models.CASCADE, related_name='users')
    acc_username = models.CharField(max_length=100)
    acc_password = models.DateField()
    user_status = models.CharField(max_length=50)
    f_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100, null=True, blank=True)
    l_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile_pic = models.CharField(max_length=255, null=True, blank=True)
    profile_bio = models.TextField(null=True, blank=True)
    profile_resume = models.CharField(max_length=255, null=True, blank=True)
    year_graduated = models.IntegerField(null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    section = models.CharField(max_length=50, null=True, blank=True)