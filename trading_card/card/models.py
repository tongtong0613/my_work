from django.db import models

# Create your models here.
class Card(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=128, verbose_name='系列')
    card_type = models.CharField(max_length=64, verbose_name='类型')
    card_set = models.CharField(max_length=64, verbose_name='具体类型')
    card_numner = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=32, verbose_name='球员')
    card_team = models.CharField(max_length=32, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')
    has_owned = models.BooleanField(default=False, verbose_name='是否拥有')
    pic_up = models.FileField(verbose_name="卡片正面", max_length=64, upload_to='card_cover', blank=True, null=True)
    pic_down = models.FileField(verbose_name="卡片背面", max_length=64, upload_to='card_cover', blank=True, null=True)

    class Meta:
        db_table = 'card'

    def __str__(self):
        return self.release_name + self.card_set