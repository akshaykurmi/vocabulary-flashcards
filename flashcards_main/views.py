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
    print(deck_name, deck_id)
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
