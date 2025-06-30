from django.db import models
from django.core.validators import RegexValidator

class AccountType(models.Model):
    account_type_id = models.AutoField(primary_key=True)
    admin = models.BooleanField(default=False)
    peso = models.BooleanField(default=False)
    user = models.BooleanField(default=False)
    coordinator = models.BooleanField(default=False)

    def __str__(self):
        return f"AccountType {self.account_type_id}"

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    account_type = models.ForeignKey('AccountType', on_delete=models.CASCADE, related_name='users')
    ctu_id = models.CharField(
        max_length=7,
        unique=True,
        validators=[RegexValidator(regex=r'^\d{7}$', message='CTU ID must be exactly 7 digits.')]
    )
    acc_username = models.CharField(max_length=100)
    acc_password = models.CharField(max_length=255)  # ✅ Should be hashed & salted!
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

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class TrackerForm(models.Model):
    tracker_form_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk and TrackerForm.objects.exists():
            raise ValueError("Only one TrackerForm instance is allowed.")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class TrackerCategory(models.Model):
    tracker_form = models.ForeignKey('TrackerForm', on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey('TrackerCategory', on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class QuestionOption(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text

class Notification(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='notifications')
    notif_type = models.CharField(max_length=100)
    notif_content = models.TextField()
    notif_date = models.DateTimeField()

    def __str__(self):
        return f"Notification for {self.user}"