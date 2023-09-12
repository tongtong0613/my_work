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
    intro = models.TextField(verbose_name='背面故事', default='')

    class Meta:
        db_table = 'card'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_set


class OtherCard(models.Model):
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
    pic_up = models.FileField(verbose_name="卡片正面", max_length=64, upload_to='other_card_cover', blank=True, null=True)
    pic_down = models.FileField(verbose_name="卡片背面", max_length=64, upload_to='other_card_cover', blank=True, null=True)
    intro = models.TextField(verbose_name='背面故事', default='')

    class Meta:
        db_table = 'other_card'

    def __str__(self):
        return self.release_name + self.card_set


class AllCard(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_numner = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'all_card'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type

class Card_2009_2010(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2009_2010'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type


class Card_2010_2011(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2010_2011'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type


class Card_2011_2012(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2011_2012'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type


class Card_2012_2013(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2012_2013'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type


class Card_2013_2014(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2013_2014'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type


class Card_2014_2015(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2014_2015'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type


class Card_2015_2016(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2015_2016'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type


class Card_2016_2017(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2016_2017'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type


class Card_2017_2018(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2017_2018'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type


class Card_2018_2019(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2018_2019'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type

class Card_2019_2020(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2019_2020'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type

class Card_2020_2021(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2020_2021'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type

class Card_2021_2022(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2021_2022'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type


class Card_2022_2023(models.Model):
    id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=32, verbose_name='发行年份')
    release_name = models.CharField(max_length=256, verbose_name='系列')
    card_type = models.CharField(max_length=256, verbose_name='类型')
    card_number = models.IntegerField(default=0, verbose_name='编号')
    card_player = models.CharField(max_length=2048, verbose_name='球员')
    card_team = models.CharField(max_length=2048, verbose_name='球队')
    card_seq = models.IntegerField(default=0, verbose_name='限量')

    class Meta:
        db_table = 'card_2022_2023'
        ordering = ['release_year']

    def __str__(self):
        return self.release_name + self.card_type