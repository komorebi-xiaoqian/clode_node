# Generated by Django 4.2.17 on 2025-01-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='isActivate',
            field=models.BooleanField(default=True, verbose_name='是否删除'),
        ),
        migrations.AlterModelTable(
            name='note',
            table='note',
        ),
    ]
