# Generated by Django 4.2.4 on 2023-12-15 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_alter_user_public_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='public_id',
            field=models.CharField(blank=True, default='', max_length=190, verbose_name='public_id'),
        ),
    ]
