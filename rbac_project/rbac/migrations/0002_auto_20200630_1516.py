# Generated by Django 2.1.11 on 2020-06-30 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='is_num',
            new_name='is_menu',
        ),
    ]
