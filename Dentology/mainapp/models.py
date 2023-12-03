from django.db import models

# Create your models here.
class Dentist(models.Model):
    first_name = models.CharField(max_length=50);
    last_name = models.CharField(max_length=50);
    email = models.EmailField(unique=True);
    phone = models.CharField(max_length=15);
    admin = models.BooleanField(default=False);

    def __str__(self):
        return self.first_name;

class Patient(models.Model):
    first_name = models.CharField(max_length=50);
    last_name = models.CharField(max_length=50);
    gender = models.TextChoices('Male', 'Female');
    email = models.EmailField(unique=True);
    phone = models.CharField(max_length=15);
    group = models.TextChoices('Adult', 'Child');
    history = models.TextField(max_length=None);
    dentist = models.ForeignKey(Dentist, on_delete=models.PROTECT);

    def __str__(self):
        return self.first_name;

class Tooth(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE);
    tooth_number = models.IntegerField();
    history = models.TextField(max_length=None);
    scheduled = models.TextField(max_length=None);
    note = models.CharField(max_length=255);
    image = models.CharField(max_length=100);

    class Meta:
        unique_together = ('patient_id', 'tooth_number');
        constraints = [
            models.CheckConstraint(
                check=models.Q(tooth_number__gte=1) & models.Q(tooth_number__lte=32),
                name="tooth_number"
            )
        ]