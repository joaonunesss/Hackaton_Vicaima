# Generated by Django 5.0.6 on 2024-05-16 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_eval_sheet_event_sheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='assi_falta_injust',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='assi_falta_just',
            field=models.IntegerField(default=3),
        ),
    ]
