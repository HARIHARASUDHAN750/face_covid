# Generated by Django 3.1 on 2020-08-30 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_app', '0002_auto_20200830_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face_photos',
            name='img_input',
            field=models.ImageField(upload_to='images_input/'),
        ),
    ]