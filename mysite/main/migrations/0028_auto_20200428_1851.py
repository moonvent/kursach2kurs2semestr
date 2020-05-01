# Generated by Django 3.0.3 on 2020-04-28 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20200428_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='id_of_reason',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Reason'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='id_of_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Country'),
        ),
        migrations.AlterField(
            model_name='medicament',
            name='id_of_pharma_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Pharma_group'),
        ),
        migrations.AlterField(
            model_name='medicament',
            name='id_of_shape',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Shape'),
        ),
    ]