# Generated by Django 5.0.1 on 2024-02-12 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Owner', '0011_alter_project_imgs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='imgs',
        ),
        migrations.AddField(
            model_name='project',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
    ]
