# Generated by Django 3.0.3 on 2020-04-28 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20200401_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='id_of_district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.District'),
        ),
    ]