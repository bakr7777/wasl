# Generated by Django 5.0.1 on 2024-02-14 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Owner', '0019_remove_projectimages_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
    ]