# Generated by Django 3.0.3 on 2020-02-25 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200224_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name_of_medicament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_medicament', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='medicament',
            name='title_of_medicament',
        ),
        migrations.AddField(
            model_name='medicament',
            name='id_of_medicament',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Name_of_medicament'),
            preserve_default=False,
        ),
    ]