# Generated by Django 4.2.4 on 2023-10-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_rename_profile_photo_png_user_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, height_field='180', null=True, upload_to='profile_photos', width_field='180'),
        ),
    ]
