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
@csrf_protect
def access_update(request):
    """
    Handles PUT requests to update access modules of a role.
    Expected data: id, accessModules (list of unique values)
    """
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


# Remove the list of access modules (ensure unique values).
@csrf_protect
def access_remove(request):
    """
    Handles PUT requests to remove access modules from a role.
    Expected data: id, accessModules (list of unique values to remove)
    """
    if request.method == "PUT":
        try:
           data = json.loads(request.body)
           role_id = data.get("id")
           acss_remove = data.get("accessModules")
           acss_list = Role.objects.filter(id=role_id).values("accessModules")[0]["accessModules"]
           for i in acss_remove:
               if i in acss_list:
                   acss_list.remove(i)
               else:
                   return JsonResponse(
                       {"message": "Access module not found"},
                       status=404
                   )
           Role.objects.filter(id=role_id).update(accessModules=acss_list)
           return JsonResponse(
                   {"message": "Access modules removed successfully"},
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
    

def role_search(request):
    """Handles GET requests to search for roles.
    Expected data: searchBy, searchValue"""
    try:
        search_by = request.GET.get("searchBy")
        search_value = request.GET.get("searchValue")

        if search_by == "roleName":
            roles = Role.objects.filter(roleName=search_value)
        elif search_by == "accessModules":
           roles = Role.objects.filter(accessModules__icontains=search_value)

        elif search_by == "active":
            roles = Role.objects.filter(active=search_value)
        else:
            return JsonResponse(
                {"message": "Invalid search field"},
                status=400
            )

        roles_list = []

        for role in roles:
            roles_list.append(
                {
                    "id": role.id,
                    "roleName": role.roleName,
                    "accessModules": role.accessModules,
                    "active": role.active
                }
            )

        return JsonResponse(
            {"roles": roles_list},
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=400
        )

    return JsonResponse(
        {"message": "Only GET method is allowed"},
        status=405
    )