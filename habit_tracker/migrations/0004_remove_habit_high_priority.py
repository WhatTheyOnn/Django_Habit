# Generated by Django 5.1.5 on 2025-01-27 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0003_habit_high_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='high_priority',
        ),
    ]
