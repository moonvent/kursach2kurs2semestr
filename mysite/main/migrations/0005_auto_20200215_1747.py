# Generated by Django 3.0.3 on 2020-02-15 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200213_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lot',
            old_name='employee',
            new_name='id_of_employee',
        ),
    ]