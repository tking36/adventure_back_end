# Generated by Django 4.1.4 on 2023-01-10 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure_db', '0002_rename_restaurant_adventure'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adventure',
            old_name='villians',
            new_name='villains',
        ),
    ]