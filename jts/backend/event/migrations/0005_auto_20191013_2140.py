# Generated by Django 2.2 on 2019-10-14 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_is_rejected'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-updated_at']},
        ),
    ]
