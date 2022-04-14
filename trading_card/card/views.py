from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Card


def index(request):
    all_cards = Card.objects.order_by('-release_year')
    context = {'all_cards': all_cards}
    return render(request, 'base.html', context)


def all_card(request):
    all_cards = Card.objects.order_by('-release_year')
    paginator = Paginator(all_cards, 10)
    current_page = request.GET.get("page", 1)
    all_cards = paginator.page(current_page)
    page_range = range(all_cards.number - 1, all_cards.number + 2)
    max_page = paginator.num_pages
    context = {'all_cards': all_cards,
               'page_range': page_range,
               'max_page': max_page,
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
    paginator = Paginator(owned_cards, 10)
    current_page = request.GET.get("page", 1)
    owned_cards = paginator.page(current_page)
    page_range = range(owned_cards.number - 1, owned_cards.number + 2)
    max_page = paginator.num_pages
    context = {'owned_cards': owned_cards,
               'page_range': page_range,
               'max_page': max_page,
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


