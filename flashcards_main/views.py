from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *


def home(request):
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
