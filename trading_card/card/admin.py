from django.contrib import admin
from .models import Card
import xadmin


# Register your models here.
class CardAdmin(object):
    list_display = ('release_name', 'card_set', 'card_player', 'card_team', 'card_seq', 'has_owned')
    search_fields = ['card_set', 'release_name']


xadmin.site.register(Card, CardAdmin)
