from django.http import JsonResponse
from .models import Users
import json
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie


@ensure_csrf_cookie
def get_csrf(request):
    return JsonResponse({
        "csrftoken": request.META.get("CSRF_COOKIE")
    })

def user_get(request):

    users = Users.objects.select_related("role").all()

    result = []

    for user in users:

        result.append({
            "id": user.id,
            "username": user.username,
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email,

            "role": {
                "roleName": user.role.roleName,
                "accessModules": user.role.accessModules
            } if user.role else None
        })

    return JsonResponse(
        result,
        safe=False
    )

# @csrf_protect
# def user_post(request):

#     try:
#         if request.method == "POST":

#             data = json.loads(request.body)
#             Users.objects.create(**data)

#             return JsonResponse(
#                 {"message": "User created successfully"},
#             status=201
#         )

#     except Exception as e:
#         return JsonResponse(
#             {"error": str(e)},
#             status=400
#         )

#     return JsonResponse(
#         {"message": "Only POST method is allowed"},
#         status=405
#     )

@csrf_protect
def user_post(request):

    try:
        if request.method == "POST":

            data = json.loads(request.body)

            role_id = data.pop("role", None)

            user = Users(
                username=data.get("username"),
                firstName=data.get("firstName"),
                lastName=data.get("lastName"),
                email=data.get("email"),
            )

            if role_id:
                user.role_id = role_id

            user.set_password(data.get("password"))

            user.save()

            return JsonResponse(
                {
                    "message": "User created successfully",
                    "id": user.id
                },
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


def user_delete(request , username):
    if request.method == "DELETE":
        try:
            Users.objects.filter(username=username).delete()
            return JsonResponse(
                {"message": "User deleted successfully"},
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


@csrf_protect
def user_put(request , id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            Users.objects.filter(id=id).update(**data)
            return JsonResponse(
                {"message": "User updated successfully"},
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