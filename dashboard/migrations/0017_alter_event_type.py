# Generated by Django 4.2.4 on 2023-11-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_remove_event_closed_dates_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.IntegerField(choices=[('1', 'PUBLIC'), ('2', 'non-business-hours'), ('3', 'unavailable')], default='1'),
        ),
    ]
