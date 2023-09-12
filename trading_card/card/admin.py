from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from xadmin import views
from .models import *
from django.db import connections, router
from django.core.exceptions import ImproperlyConfigured, ValidationError
from import_export.utils import atomic_if_using_transaction
import xadmin
import collections


# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = ('release_year', 'release_name', 'card_set', 'card_player', 'card_team', 'card_seq', 'has_owned')
    search_fields = ['card_set', 'release_name']


class OtherCardAdmin(admin.ModelAdmin):
    list_display = ('release_year', 'release_name', 'card_set', 'card_player', 'card_team', 'card_seq', 'has_owned')
    search_fields = ['card_set', 'release_name']


class Card_2009_2010Resource(resources.ModelResource):
    class Meta:
        model = Card_2009_2010

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2009_2010':
            raise ValueError("Please import a list which release_year is 2009_2010")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2009_2010Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2009_2010Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2009_2010Resource


class Card_2010_2011Resource(resources.ModelResource):
    class Meta:
        model = Card_2010_2011

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2010-2011':
            raise ValueError("Please import a list which release_year is 2010-2011")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2010_2011Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2010_2011Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2010_2011Resource


class Card_2011_2012Resource(resources.ModelResource):
    class Meta:
        model = Card_2011_2012

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2011-2012':
            raise ValueError("Please import a list which release_year is 2011-2012")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2011_2012Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2011_2012Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2011_2012Resource


class Card_2012_2013Resource(resources.ModelResource):
    class Meta:
        model = Card_2012_2013

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2012-2013':
            raise ValueError("Please import a list which release_year is 2012-2013")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2012_2013Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2012_2013Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2012_2013Resource


class Card_2013_2014Resource(resources.ModelResource):
    class Meta:
        model = Card_2013_2014

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2013-2014':
            raise ValueError("Please import a list which release_year is 2013-2014")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2013_2014Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2013_2014Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2013_2014Resource


class Card_2014_2015Resource(resources.ModelResource):
    class Meta:
        model = Card_2014_2015

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2014-2015':
            raise ValueError("Please import a list which release_year is 2014-2015")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2014_2015Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2014_2015Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2014_2015Resource


class Card_2015_2016Resource(resources.ModelResource):
    class Meta:
        model = Card_2015_2016

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2015-2016':
            raise ValueError("Please import a list which release_year is 2015-2016")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2015_2016Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2015_2016Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2015_2016Resource


class Card_2016_2017Resource(resources.ModelResource):
    class Meta:
        model = Card_2016_2017

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2016-2017':
            raise ValueError("Please import a list which release_year is 2016-2017")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2016_2017Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2016_2017Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2016_2017Resource


class Card_2017_2018Resource(resources.ModelResource):
    class Meta:
        model = Card_2017_2018

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2017-2018':
            raise ValueError("Please import a list which release_year is 2017-2018")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2017_2018Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2017_2018Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2017_2018Resource


class Card_2018_2019Resource(resources.ModelResource):
    class Meta:
        model = Card_2018_2019

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2018-2019':
            raise ValueError("Please import a list which release_year is 2018-2019")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2018_2019Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2018_2019Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2018_2019Resource


class Card_2019_2020Resource(resources.ModelResource):
    class Meta:
        model = Card_2019_2020

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2019-2020':
            raise ValueError("Please import a list which release_year is 2019-2020")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2019_2020Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2019_2020Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2019_2020Resource


class Card_2020_2021Resource(resources.ModelResource):
    class Meta:
        model = Card_2020_2021

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2020-2021':
            raise ValueError("Please import a list which release_year is 2020-2021")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2020_2021Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2020_2021Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2020_2021Resource


class Card_2021_2022Resource(resources.ModelResource):
    class Meta:
        model = Card_2021_2022

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']
        
        release_year = file_name[10:14]
        
        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2021-2022':
            raise ValueError("Please import a list which release_year is 2021-2022")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2021_2022Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2021_2022Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2021_2022Resource


class Card_2022_2023Resource(resources.ModelResource):
    class Meta:
        model = Card_2022_2023

        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id',)

        fields = (
            'id',
            'release_year',
            'release_name',
            'card_type',
            'card_number',
            'card_player',
            'card_team',
            'card_seq',
        )

    def before_import_row(self, row, **kwargs):
        new_row = collections.OrderedDict()
        file_name = kwargs['file_name']

        release_year = file_name[10:14]

        release_year = release_year + '-' + str(int(release_year) + 1)
        if release_year != '2022-2023':
            raise ValueError("Please import a list which release_year is 2022-2023")
        release_name = file_name.split('(')[0][14:]
        if 'Panini' in release_name:
            release_name = 'Panini - ' + release_name[6:]
        elif 'Donruss' in release_name:
            release_name = 'Donruss - ' + release_name[7:]
        else:
            release_name = 'Panini - ' + release_name[7:]
        new_row['release_year'] = release_year
        new_row['release_name'] = release_name
        new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
        new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
        new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
        new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
        new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
        print(new_row)
        return new_row


class Card_2022_2023Admin(ImportExportModelAdmin):
    list_display = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
        'card_seq',
    ]

    ordering = ['id']

    search_fields = [
        'release_year',
        'release_name',
        'card_type',
        'card_player',
        'card_team',
    ]

    list_filter = [
        'release_year',
        'release_name',
        'card_type',
        'card_number',
        'card_player',
        'card_team',
    ]

    list_per_page = 100

    import_export_args = {
        'import_resource_class': Card_2022_2023Resource,
        # 'export_resource_class': ProductInfoResource,
    }

    resource_class = Card_2022_2023Resource

# class AllCardResource(resources.ModelResource):
#
#     class Meta:
#         model = AllCard
#
#         skip_unchanged = True
#         # 导入数据时，如果该条数据未修改过，则会忽略
#         report_skipped = True
#         # 在导入预览页面中显示跳过的记录
#
#         import_id_fields = ('id',)
#         # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id
#
#         fields = (
#             'id',
#             'release_year',
#             'release_name',
#             'card_type',
#             'card_number',
#             'card_player',
#             'card_team',
#             'card_seq',
#         )
#         # 白名单
#
#         # exclude = (
#         #     'create_time',
#         #     'update_time',
#         # )
#         # # 黑名单
#
#     def before_import_row(self, row, **kwargs):
#         new_row = collections.OrderedDict()
#         file_name = kwargs['file_name']
#         
#         release_year = file_name[10:14]
#         
#         release_year = release_year + '-' + str(int(release_year) + 1)
#         release_name = file_name.split('(')[0][14:]
#         if 'Panini' in release_name:
#             release_name = 'Panini - ' + release_name[6:]
#         elif 'Donruss' in release_name:
#             release_name = 'Donruss - ' + release_name[7:]
#         else:
#             release_name = 'Panini - ' + release_name[7:]
#         new_row['release_year'] = release_year
#         new_row['release_name'] = release_name
#         new_row['card_type'] = row['Card Set'] if 'Card Set' in row.keys() else 'unknown'
#         new_row['card_number'] = row['Number'] if 'Number' in row.keys() else 'unknown'
#         new_row['card_player'] = row['Player'] if 'Player' in row.keys() else 'unknown'
#         new_row['card_team'] = row['Team'] if 'Team' in row.keys() else 'unknown'
#         new_row['card_seq'] = row['Seq.'] if 'Seq.' in row.keys() else 'unknown'
#         print(new_row)
#         return new_row
#
#
#
# class AllCardAdmin(ImportExportModelAdmin):
#     list_display = [
#         'release_year',
#         'release_name',
#         'card_type',
#         'card_number',
#         'card_player',
#         'card_team',
#         'card_seq',
#     ]
#     # 要显示的字段列表
#
#     ordering = ['id']
#     # 按照id顺序排列，如果是倒序-id
#
#     search_fields = [
#         'release_year',
#         'release_name',
#         'card_type',
#         'card_player',
#         'card_team',
#     ]
#     # 要搜索的字段
#
#     list_filter = [
#         'release_year',
#         'release_name',
#         'card_type',
#         'card_number',
#         'card_player',
#         'card_team',
#     ]
#     # 要筛选的字段
#
#     # show_detail_fields = ['product_name', 'product_picture']
#     # # 要展示详情的字段
#     #
#     # list_editable = ['product_name', 'product_picture',
#     #                  'product_describe', 'product_manager']
#     # # 列表可直接修改的字段
#
#     list_per_page = 100
#     # 分页
#
#     # model_icon = 'fa fa-laptop'
#     # 配置模型图标，也可以在GlobalSetting里面配置
#
#     import_export_args = {
#         'import_resource_class': AllCardResource,
#         # 'export_resource_class': ProductInfoResource,
#     }
#     # 配置导入按钮
#
#     resource_class = AllCardResource


# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True
#     # 开启主题自由切换
#
#
# class GlobalSetting(object):
#     global_search_models = [AllCard]
#     # 配置全局搜索选项，默认搜索组、用户、日志记录
#     site_title = "卡片List"
#     # 标题
#     site_footer = "List"
#     # 页脚
#
#     menu_style = "accordion"
#     # 左侧菜单收缩功能
#     apps_icons = {
#         "product": "fa fa-music",
#     }
#     # 配置应用图标，即一级菜单图标
#     global_models_icon = {
#         AllCard: "fa fa-film",
#     }
#     # 配置模型图标，即二级菜单图标


# xadmin.site.register(Card, CardAdmin)
# xadmin.site.register(OtherCard, OtherCardAdmin)
# xadmin.site.register(AllCard, AllCardAdmin)

# admin.site.register(Card, CardAdmin)
# admin.site.register(OtherCard, OtherCardAdmin)
admin.site.register(Card_2009_2010, Card_2009_2010Admin)
admin.site.register(Card_2010_2011, Card_2010_2011Admin)
admin.site.register(Card_2011_2012, Card_2011_2012Admin)
admin.site.register(Card_2012_2013, Card_2012_2013Admin)
admin.site.register(Card_2013_2014, Card_2013_2014Admin)
admin.site.register(Card_2014_2015, Card_2014_2015Admin)
admin.site.register(Card_2015_2016, Card_2015_2016Admin)
admin.site.register(Card_2016_2017, Card_2016_2017Admin)
admin.site.register(Card_2017_2018, Card_2017_2018Admin)
admin.site.register(Card_2018_2019, Card_2018_2019Admin)
admin.site.register(Card_2019_2020, Card_2019_2020Admin)
admin.site.register(Card_2020_2021, Card_2020_2021Admin)
admin.site.register(Card_2021_2022, Card_2021_2022Admin)
admin.site.register(Card_2022_2023, Card_2022_2023Admin)

# xadmin.site.register(views.BaseAdminView, BaseSetting)
# xadmin.site.register(views.CommAdminView, GlobalSetting)

admin.site.site_header = '球星卡Checklist'
admin.site.site_title = 'Checklist'
admin.site.index_title = '3'
