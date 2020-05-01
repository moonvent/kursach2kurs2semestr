# Generated by Django 3.0.3 on 2020-04-28 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20200428_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='title_of_country',
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='name_of_medicament',
            name='title_of_medicament',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='pharma_group',
            name='title_of_pharma_group',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='reason',
            name='title_of_reason',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='shape',
            name='title_of_shape',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='title_of_type',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]