# Generated by Django 5.1.1 on 2024-11-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='picture',
            field=models.ImageField(null=True, upload_to='vehicle_images'),
        ),
    ]