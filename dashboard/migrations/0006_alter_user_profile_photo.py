# Generated by Django 4.2.4 on 2023-10-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_user_company_user_position_user_profile_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, height_field='180', upload_to='core/media/profile_photos', width_field='180'),
        ),
    ]
