from django.urls import path, re_path

from . import views

urlpatterns = [
    path('card/', views.index, name='index'),
    path("all_card/", views.all_card, name="all_card"),
    path("card/<int:card_id>/", views.card, name="card"),
    path("owned_card/", views.owned_card, name="owned_card"),
    path("no_owned_card/", views.no_owned_card, name="no_owned_card"),
]