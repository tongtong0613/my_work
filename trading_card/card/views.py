from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, reverse
from django.core.paginator import Paginator

from .models import Card, OtherCard


def index(request):
    all_cards = Card.objects.order_by('-release_year')
    context = {'all_cards': all_cards}
    return render(request, 'base.html', context)


def all_card(request):
    all_cards = Card.objects.order_by('-release_year')
    year = Card.objects.values('release_year').distinct().order_by('release_year')
    name = Card.objects.values('release_name').distinct().order_by('release_name')
    team = Card.objects.values('card_team').distinct().order_by('card_team')
    paginator = Paginator(all_cards, 10)
    current_page = request.GET.get("page", 1)
    all_cards = paginator.page(current_page)
    page_range = range(all_cards.number - 1, all_cards.number + 2)
    max_page = paginator.num_pages
    context = {'all_cards': all_cards,
               'page_range': page_range,
               'max_page': max_page,
               'name': name,
               'team': team,
               'year': year,
               }
    return render(request, 'all_card.html', context)


def card(request, card_id):
    card = Card.objects.get(pk=card_id)
    release_name = card.release_name
    card_set = card.card_set
    card_player = card.card_player
    card_team = card.card_team
    card_seq = card.card_seq
    has_owned = card.has_owned
    return render(request, "card.html", locals())


def owned_card(request):
    owned_cards = Card.objects.filter(has_owned=1)
    year = owned_cards.values('release_year').distinct().order_by('release_year')
    name = owned_cards.values('release_name').distinct().order_by('release_name')
    team = owned_cards.values('card_team').distinct().order_by('card_team')
    paginator = Paginator(owned_cards, 10)
    current_page = request.GET.get("page", 1)
    owned_cards = paginator.page(current_page)
    page_range = range(owned_cards.number - 1, owned_cards.number + 2)
    max_page = paginator.num_pages
    context = {'owned_cards': owned_cards,
               'page_range': page_range,
               'max_page': max_page,
               'name': name,
               'team': team,
               'year': year,
               }
    return render(request, 'owned_card.html', context)


def no_owned_card(request):
    no_owned_cards = Card.objects.filter(has_owned=0)
    paginator = Paginator(no_owned_cards, 10)
    current_page = request.GET.get("page", 1)
    no_owned_cards = paginator.page(current_page)
    page_range = range(no_owned_cards.number - 1, no_owned_cards.number + 2)
    max_page = paginator.num_pages
    context = {'no_owned_cards': no_owned_cards,
               'page_range': page_range,
               'max_page': max_page,
               }
    return render(request, 'no_owned_card.html', context)


def other_owned(request):
    all_cards = OtherCard.objects.order_by('-release_year')
    paginator = Paginator(all_cards, 10)
    current_page = request.GET.get("page", 1)
    all_cards = paginator.page(current_page)
    page_range = range(all_cards.number - 1, all_cards.number + 2)
    max_page = paginator.num_pages
    year = OtherCard.objects.values('release_year').distinct().order_by('release_year')
    name = OtherCard.objects.values('release_name').distinct().order_by('release_name')
    team = OtherCard.objects.values('card_team').distinct().order_by('card_team')
    context = {'other_owned': all_cards,
               'page_range': page_range,
               'max_page': max_page,
               'name': name,
               'team': team,
               'year': year,
               }
    return render(request, 'other_owned.html', context)


def other_card(request, card_id):
    card = OtherCard.objects.get(pk=card_id)
    release_name = card.release_name
    card_set = card.card_set
    card_player = card.card_player
    card_team = card.card_team
    card_seq = card.card_seq
    has_owned = card.has_owned
    return render(request, "card.html", locals())


def filter(request):
    conditions, conditions_zh = {}, {}
    get_url_use = []
    release_year = request.GET.get('svalue_1', '')
    release_name = request.GET.get('svalue_2', '')
    card_team = request.GET.get('svalue_3', '')
    if release_year:
        conditions['release_year'] = release_year
        conditions_zh['年份'] = release_year
        get_url_use.append('svalue_1=' + release_year)
    if release_name:
        conditions['release_name'] = release_name
        conditions_zh['系列'] = release_name
        get_url_use.append('svalue_2=' + release_name)
    if card_team:
        conditions['card_team'] = card_team
        conditions_zh['球队'] = card_team
        get_url_use.append('svalue_3=' + card_team)
    all_cards = Card.objects.filter(**conditions).values()
    paginator = Paginator(all_cards, 10)
    current_page = request.GET.get("page", 1)
    all_cards = paginator.page(current_page)
    page_range = range(all_cards.number - 1, all_cards.number + 2)
    max_page = paginator.num_pages
    year = Card.objects.values('release_year').distinct().order_by('release_year')
    name = Card.objects.values('release_name').distinct().order_by('release_name')
    team = Card.objects.values('card_team').distinct().order_by('card_team')
    context = {'filter_cards': all_cards,
               'page_range': page_range,
               'max_page': max_page,
               'name': name,
               'team': team,
               'year': year,
               'conditions_zh': conditions_zh,
               'get_url_use': get_url_use
               }
    print(context)
    return render(request, 'filter_card.html', context)


def filter_other(request):
    conditions, conditions_zh = {}, {}
    get_url_use = []
    release_year = request.GET.get('svalue_1', '')
    release_name = request.GET.get('svalue_2', '')
    card_team = request.GET.get('svalue_3', '')
    if release_year:
        conditions['release_year'] = release_year
        conditions_zh['年份'] = release_year
        get_url_use.append('svalue_1=' + release_year)
    if release_name:
        conditions['release_name'] = release_name
        conditions_zh['系列'] = release_name
        get_url_use.append('svalue_2=' + release_name)
    if card_team:
        conditions['card_team'] = card_team
        conditions_zh['球队'] = card_team
        get_url_use.append('svalue_3=' + card_team)
    all_cards = OtherCard.objects.filter(**conditions).values()
    paginator = Paginator(all_cards, 10)
    current_page = request.GET.get("page", 1)
    all_cards = paginator.page(current_page)
    page_range = range(all_cards.number - 1, all_cards.number + 2)
    max_page = paginator.num_pages
    year = OtherCard.objects.values('release_year').distinct().order_by('release_year')
    name = OtherCard.objects.values('release_name').distinct().order_by('release_name')
    team = OtherCard.objects.values('card_team').distinct().order_by('card_team')
    context = {'filter_cards': all_cards,
               'page_range': page_range,
               'max_page': max_page,
               'name': name,
               'team': team,
               'year': year,
               'conditions_zh': conditions_zh,
               'get_url_use': get_url_use
               }
    print(context)
    return render(request, 'filter_other_card.html', context)


def filter_owned(request):
    conditions, conditions_zh = {}, {}
    get_url_use = []
    release_year = request.GET.get('svalue_1', '')
    release_name = request.GET.get('svalue_2', '')
    card_team = request.GET.get('svalue_3', '')
    conditions['has_owned'] = 1
    conditions_zh['已拥有'] = 'True'
    if release_year:
        conditions['release_year'] = release_year
        conditions_zh['年份'] = release_year
        get_url_use.append('svalue_1=' + release_year)
    if release_name:
        conditions['release_name'] = release_name
        conditions_zh['系列'] = release_name
        get_url_use.append('svalue_2=' + release_name)
    if card_team:
        conditions['card_team'] = card_team
        conditions_zh['球队'] = card_team
        get_url_use.append('svalue_3=' + card_team)
    all_cards = Card.objects.filter(**conditions).values()
    # del conditions['has_owned']
    paginator = Paginator(all_cards, 10)
    current_page = request.GET.get("page", 1)
    all_cards = paginator.page(current_page)
    page_range = range(all_cards.number - 1, all_cards.number + 2)
    max_page = paginator.num_pages
    owned_cards = Card.objects.filter(has_owned=1)
    year = owned_cards.values('release_year').distinct().order_by('release_year')
    name = owned_cards.values('release_name').distinct().order_by('release_name')
    team = owned_cards.values('card_team').distinct().order_by('card_team')
    context = {'filter_cards': all_cards,
               'page_range': page_range,
               'max_page': max_page,
               'name': name,
               'team': team,
               'year': year,
               'conditions_zh': conditions_zh,
               'get_url_use': get_url_use
               }
    print(context)
    return render(request, 'filter_owned.html', context)

