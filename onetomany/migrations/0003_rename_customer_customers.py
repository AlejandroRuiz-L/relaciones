# Generated by Django 5.0.2 on 2024-03-16 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onetomany', '0002_employees'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Customers',
        ),
    ]
