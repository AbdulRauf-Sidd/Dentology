# Generated by Django 4.2.7 on 2023-12-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentist',
            name='password',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
