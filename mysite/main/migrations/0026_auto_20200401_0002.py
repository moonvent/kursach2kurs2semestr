# Generated by Django 3.0.3 on 2020-03-31 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20200331_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='id_of_reason',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Reason'),
        ),
    ]
