# Generated by Django 4.2 on 2023-04-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_sighting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sighting',
            old_name='location',
            new_name='time',
        ),
        migrations.AlterField(
            model_name='sighting',
            name='date',
            field=models.DateTimeField(verbose_name='Finch Sighting'),
        ),
    ]
