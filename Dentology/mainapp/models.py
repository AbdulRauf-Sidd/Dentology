from django.db import models

# Create your models here.
class Dentist(models.Model):
    id = models.AutoField(primary_key=True);
    first_name = models.CharField(max_length=50);
    last_name = models.CharField(max_length=50);
    email = models.EmailField(unique=True);
    password = models.CharField(max_length=50);
    phone = models.CharField(max_length=15);
    admin = models.BooleanField(default=False);
    

    def __str__(self):
        return self.first_name;

class Patient(models.Model):

    male = 'male'
    female = 'female'

    gender_choice = [
        (male, 'Male'),
        (female, 'Female'),
    ]

    child = "child";
    adult = "adult";

    group_choice = [
        (child, "Child"),
        (adult, "Adult")
    ]

    id = models.AutoField(primary_key=True);
    first_name = models.CharField(max_length=50);
    last_name = models.CharField(max_length=50);
    gender = models.CharField(max_length=10, choices=gender_choice);
    email = models.EmailField(unique=True, null=True, blank=True);
    phone = models.CharField(max_length=15, null=True, blank=True);
    group = models.CharField(max_length=10, choices=group_choice);
    history = models.TextField(max_length=None, null=True, blank=True);
    dentist = models.ForeignKey(Dentist, on_delete=models.PROTECT);

    def __str__(self):
        return self.first_name;

class Tooth(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE);
    tooth_number = models.IntegerField();
    history = models.TextField(max_length=None, null=True, blank=True);
    scheduled = models.TextField(max_length=None, null=True, blank=True);
    note = models.CharField(max_length=255, null=True, blank=True);
    image = models.CharField(max_length=100);

    class Meta:
        unique_together = ('patient_id', 'tooth_number');
        constraints = [
            models.CheckConstraint(
                check=models.Q(tooth_number__gte=1) & models.Q(tooth_number__lte=32),
                name="tooth_number"
            )
        ]