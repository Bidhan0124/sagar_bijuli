# Generated by Django 4.2.2 on 2025-04-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='electrician',
            name='contact',
            field=models.SmallIntegerField(blank=True, default='9841234567', help_text='phone number'),
        ),
    ]
