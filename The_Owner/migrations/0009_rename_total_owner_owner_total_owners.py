# Generated by Django 5.0.1 on 2024-02-12 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('The_Owner', '0008_rename_total_owner_owner_total_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='total_owner',
            new_name='total_owners',
        ),
    ]
