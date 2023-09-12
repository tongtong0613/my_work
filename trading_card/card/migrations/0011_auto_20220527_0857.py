# Generated by Django 3.1.7 on 2022-05-27 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0010_auto_20220525_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcard',
            name='card_player',
            field=models.CharField(max_length=256, verbose_name='球员'),
        ),
        migrations.AlterField(
            model_name='allcard',
            name='card_team',
            field=models.CharField(max_length=256, verbose_name='球队'),
        ),
        migrations.AlterField(
            model_name='allcard',
            name='card_type',
            field=models.CharField(max_length=256, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='allcard',
            name='release_name',
            field=models.CharField(max_length=256, verbose_name='系列'),
        ),
    ]
