# Generated by Django 3.0.2 on 2020-08-30 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face_photos',
            name='img_output',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='images_output/'),
        ),
    ]