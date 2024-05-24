# Generated by Django 5.0 on 2024-05-15 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Owner', '0037_alter_owner_address_alter_owner_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='address',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='owner',
            name='photo',
            field=models.ImageField(blank=True, upload_to='owners/%Y/%m/%d/'),
        ),
    ]
