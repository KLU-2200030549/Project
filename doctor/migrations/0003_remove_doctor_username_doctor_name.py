# Generated by Django 4.1.13 on 2024-04-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_remove_doctor_name_doctor_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='username',
        ),
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
