from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home, name="Home"),
    url('^groups/$', views.groups, name="Groups"),
    url("^addGroup/", views.add_group, name="Add Group"),
    url("^deleteGroup/", views.delete_group, name="Delete Group"),
    url("^editGroup/", views.edit_group, name="Edit Group"),
    url("^groups/(?P<group_id>[\d]+)/decks", views.decks, name="Decks"),
    url("^groups/(?P<group_id>[\d]+)/addDeck", views.add_deck, name="Add Deck"),
    url("^deleteDeck/", views.delete_deck, name="Delete Deck"),
    url("^editDeck/", views.edit_deck, name="Edit Deck"),
]
