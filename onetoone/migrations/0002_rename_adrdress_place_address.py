# Generated by Django 5.0.2 on 2024-03-16 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onetoone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='adrdress',
            new_name='address',
        ),
    ]
