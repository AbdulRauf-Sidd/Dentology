from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import Patient, Tooth

@receiver(post_save, sender=Patient)
def create_tooth_instances(sender, instance, created, **kwargs):
    if created:
        # The client instance is newly created
        with transaction.atomic():
            # Use a transaction to ensure all 30 Tooth instances are created or none at all
            for tooth_number in range(1, 33):
                Tooth.objects.create(patient_id=instance, tooth_number=tooth_number)
