from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Role
from django.views.decorators.csrf import csrf_protect
import json
# Create your views here.

def role_page(request):
    return HttpResponse("Hello, this is the role page")

def role_get(request):
    roles = Role.objects.all().values()
    return JsonResponse(
        list(roles),
        safe=False
    )


@csrf_protect
def role_post(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            Role.objects.create(**data)
            return JsonResponse(
                {"message": "Role created successfully"},
                status=201
            )
    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=400
        )
    return JsonResponse(
        {"message": "Only POST method is allowed"},
        status=405
    )


@csrf_protect
def role_put(request , id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            Role.objects.filter(id=id).update(**data)
            return JsonResponse(
                {"message": "Role updated successfully"},
                status=200
            )
        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )
    return JsonResponse(
        {"message": "Only PUT method is allowed"},
        status=405
    )


def role_delete(request , id):
    if request.method == "DELETE":
        try:
            Role.objects.filter(id=id).delete()
            return JsonResponse(
                {"message": "Role deleted successfully"},
                status=200
            )
        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )
    return JsonResponse(
        {"message": "Only DELETE method is allowed"},
        status=405
    )


