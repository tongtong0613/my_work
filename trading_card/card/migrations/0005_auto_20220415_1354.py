# Generated by Django 3.1.7 on 2022-04-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_othercard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='othercard',
            name='pic_down',
            field=models.FileField(blank=True, max_length=64, null=True, upload_to='other_card_cover', verbose_name='卡片背面'),
        ),
        migrations.AlterField(
            model_name='othercard',
            name='pic_up',
            field=models.FileField(blank=True, max_length=64, null=True, upload_to='other_card_cover', verbose_name='卡片正面'),
        ),
    ]
