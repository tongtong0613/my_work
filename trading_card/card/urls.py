from django.urls import path, re_path

from . import views

urlpatterns = [
    path('card/', views.index, name='index'),
    path("all_card/", views.all_card, name="all_card"),
    path("card/<int:card_id>/", views.card, name="card"),
    path("owned_card/", views.owned_card, name="owned_card"),
    path("no_owned_card/", views.no_owned_card, name="no_owned_card"),
    path("other_owned/", views.other_owned, name="other_owned"),
    path("other_card/<int:card_id>/", views.other_card, name="other_card"),
    path("all_card/filter/", views.filter, name="filter"),
    path("other_owned/filter_other/", views.filter_other, name="filter_other"),
    path("owned_card/filter_owned/", views.filter_owned, name="filter_owned"),
]