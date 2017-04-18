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
