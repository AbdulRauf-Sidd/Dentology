from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Dentist);
admin.site.register(models.Patient);
admin.site.register(models.Tooth);