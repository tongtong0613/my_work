# Generated by Django 3.1.7 on 2022-04-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_auto_20220413_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='intro',
            field=models.TextField(default='', verbose_name='背面故事'),
        ),
    ]