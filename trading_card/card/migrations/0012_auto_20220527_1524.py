# Generated by Django 3.1.7 on 2022-05-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0011_auto_20220527_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcard',
            name='card_player',
            field=models.CharField(max_length=2048, verbose_name='球员'),
        ),
    ]
