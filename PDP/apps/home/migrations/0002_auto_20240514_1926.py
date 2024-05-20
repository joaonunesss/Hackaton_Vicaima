# Generated by Django 3.2.12 on 2024-05-14 19:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborators',
            name='Ano',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
        ),
        migrations.AlterField(
            model_name='collaborators',
            name='Data',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
        ),
        migrations.AlterField(
            model_name='collaborators',
            name='DirUni',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='collaborators',
            name='FaltaInjust',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='collaborators',
            name='FaltaJust',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='collaborators',
            name='NumAvali',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='collaborators',
            name='NumColab',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
