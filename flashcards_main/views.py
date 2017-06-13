from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *


def home(request):
    return redirect('groups/')


def groups(request):
    data = {"groups": Group.objects.all()}
    return render(request, "flashcards_main/groups.html", data)


@csrf_exempt
def add_group(request):
    group_name = request.POST.get("groupName", "")
    if group_name == "":
        return JsonResponse({"success": False, "errorMessage": "The Group's name cannot be empty"})
    if Group.objects.filter(name=group_name).exists():
        return JsonResponse({"success": False, "errorMessage": "Group with given name already exists"})
    group = Group(name=group_name)
    group.save()
    return JsonResponse({"success": True})


@csrf_exempt
def delete_group(request):
    group_id = request.POST.get("groupId", None)
    if not group_id:
        return JsonResponse({"success": False, "errorMessage": "This Group cannot be identified"})
    if not Group.objects.filter(id=group_id).exists():
        return JsonResponse({"success": False, "errorMessage": "This Group does not exist"})
    group = Group.objects.get(id=group_id)
    group.delete()
    return JsonResponse({"success": True})


@csrf_exempt
def edit_group(request):
    group_id = request.POST.get("groupId", None)
    group_name = request.POST.get("groupName", "")
    if not group_id:
        return JsonResponse({"success": False, "errorMessage": "This Group cannot be identified"})
    if not Group.objects.filter(id=group_id).exists():
        return JsonResponse({"success": False, "errorMessage": "This Group does not exist"})
    if group_name == "":
        return JsonResponse({"success": False, "errorMessage": "The Group's name cannot be empty"})
    if Group.objects.filter(name=group_name).exists():
        return JsonResponse({"success": False, "errorMessage": "Group with given name already exists"})
    group = Group(id=group_id, name=group_name)
    group.save()
    return JsonResponse({"success": True})


def decks(request, group_id):
    data = {"decks": Deck.objects.filter(group_id=group_id)}
    return render(request, "flashcards_main/decks.html", data)


@csrf_exempt
def add_deck(request, group_id):
    deck_name = request.POST.get("deckName", "")
    if deck_name == "":
        return JsonResponse({"success": False, "errorMessage": "The Deck's name cannot be empty"})
    if Deck.objects.filter(name=deck_name).exists():
        return JsonResponse({"success": False, "errorMessage": "Deck with given name already exists"})
    deck = Deck(name=deck_name, group_id=group_id)
    deck.save()
    return JsonResponse({"success": True})


@csrf_exempt
def delete_deck(request):
    deck_id = request.POST.get("deckId", None)
    if not deck_id:
        return JsonResponse({"success": False, "errorMessage": "This Deck cannot be identified"})
    if not Deck.objects.filter(id=deck_id).exists():
        return JsonResponse({"success": False, "errorMessage": "This Deck does not exist"})
    deck = Deck.objects.get(id=deck_id)
    deck.delete()
    return JsonResponse({"success": True})


@csrf_exempt
def edit_deck(request):
    deck_id = request.POST.get("deckId", None)
    deck_name = request.POST.get("deckName", "")
    if not deck_id:
        return JsonResponse({"success": False, "errorMessage": "This Deck cannot be identified"})
    if not Deck.objects.filter(id=deck_id).exists():
        return JsonResponse({"success": False, "errorMessage": "This Deck does not exist"})
    if deck_name == "":
        return JsonResponse({"success": False, "errorMessage": "The Deck's name cannot be empty"})
    if Deck.objects.filter(name=deck_name).exists():
        return JsonResponse({"success": False, "errorMessage": "Deck with given name already exists"})
    Deck.objects.filter(id=deck_id).update(name=deck_name)
    return JsonResponse({"success": True})


def cards(request, deck_id):
    data = {"cards": FlashCard.objects.filter(deck_id=deck_id)}
    return render(request, "flashcards_main/cards.html", data)


@csrf_exempt
def add_card(request, deck_id):
    word = request.POST.get("cardWord", "")
    definition = request.POST.get("cardDefinition", "")
    sentence = request.POST.get("cardSentence", "")
    mnemonic = request.POST.get("cardMnemonic", "")
    if FlashCard.objects.filter(word=word).exists():
        c = FlashCard.objects.filter(word=word)[0]
        card = FlashCard(word=c.word, definition=c.definition, sample_sentence=c.sample_sentence,
                         mnemonic=c.mnemonic, deck_id=deck_id)
        card.save()
        return JsonResponse({"success": True})
    if word == "" or definition == "":
        return JsonResponse({"success": False, "errorMessage": "The Card's word/definition cannot be empty"})
    card = FlashCard(word=word, definition=definition, sample_sentence=sentence, mnemonic=mnemonic, deck_id=deck_id)
    card.save()
    return JsonResponse({"success": True})


@csrf_exempt
def delete_card(request):
    card_id = request.POST.get("cardId", None)
    if not card_id:
        return JsonResponse({"success": False, "errorMessage": "This Card cannot be identified"})
    if not FlashCard.objects.filter(id=card_id).exists():
        return JsonResponse({"success": False, "errorMessage": "This Card does not exist"})
    card = FlashCard.objects.get(id=card_id)
    card.delete()
    return JsonResponse({"success": True})


@csrf_exempt
def edit_card(request):
    card_id = request.POST.get("cardId", None)
    word = request.POST.get("editedCardWord", "")
    definition = request.POST.get("editedCardDefinition", "")
    sentence = request.POST.get("editedCardSentence", "")
    mnemonic = request.POST.get("editedCardMnemonic", "")
    if not card_id:
        return JsonResponse({"success": False, "errorMessage": "This Card cannot be identified"})
    if not FlashCard.objects.filter(id=card_id).exists():
        return JsonResponse({"success": False, "errorMessage": "This Card does not exist"})
    if word == "" or definition == "":
        return JsonResponse({"success": False, "errorMessage": "The Card's word/definition cannot be empty"})
    FlashCard.objects.filter(id=card_id).update(word=word, definition=definition, sample_sentence=sentence,
                                                mnemonic=mnemonic)
    return JsonResponse({"success": True})
