# Generated by Django 4.2.7 on 2023-12-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_patient_email_alter_patient_history_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='group',
            field=models.CharField(choices=[('child', 'Child'), ('adult', 'Adult')], default='adult', max_length=10),
            preserve_default=False,
        ),
    ]
