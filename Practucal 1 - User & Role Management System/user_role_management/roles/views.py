from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Role
from django.views.decorators.csrf import csrf_protect
import json
# Create your views here.

#GET request to get all the roles
def role_get(request):
    """Handles GET requests to retrieve all roles."""
    roles = Role.objects.all().values()
    return JsonResponse(
        list(roles),
        safe=False
    )

#POST request to create a new role
@csrf_protect
def role_post(request):
    """Handles POST requests to create a new role.
    Expects JSON data with fields: roleName, accessModules, active"""
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

#PUT request to update a role
@csrf_protect
def role_put(request , id):
    """Handles PUT requests to update a role.
    Expects JSON data with fields: roleName, accessModules, active"""
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

#DELETE request to delete a role
def role_delete(request , id):
    """Handles DELETE requests to delete a role."""
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

# Update the list of access modules (ensure unique values).
def access_update(request):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            role_id  = data.get("id")
            access_modules = list(set(data.get("accessModules")))
            role_obj = Role.objects.filter(id=role_id ).update(accessModules=access_modules)
            if not role_obj:
                return JsonResponse(
                    {"message": "Role not found"},
                    status=404
                )
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
