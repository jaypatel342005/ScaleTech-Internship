from django.http import JsonResponse
from .models import Users
import json
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.db.models import When, Case, Value, CharField



@ensure_csrf_cookie
def get_csrf(request):
    """Returns the CSRF token."""
    return JsonResponse({
        "csrftoken": request.META.get("CSRF_COOKIE")
    })

#GET request to get all the users
def user_get(request):
    """Handles GET requests to retrieve all users."""

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



#POST request to create a new user
@csrf_protect
def user_post(request):
    """Handles POST requests to create a new user.
    Expects JSON data with fields: username, firstName, lastName, email, password, role"""
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


#DELETE request to delete a user
def user_delete(request , username):
    """Handles DELETE requests to delete a user."""
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


#PUT request to update a user
@csrf_protect
def user_put(request , id):
    """Handles PUT requests to update a user."""
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


#PUT request to update multiple users same data
@csrf_protect
def update_multiple(request):
    """Handles PUT requests to update multiple users.
    Expected data: ids, field/data (field to update)
    """
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            list = data["ids"]
            val = data["data"]
            # for id in list:
            #     Users.objects.filter(id=id).update(**val)

            Users.objects.filter(id__in=list).update(**val)
            return JsonResponse(
                {"message": "Users updated successfully"},
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


#PUT request to update multiple users with diffrent data in single database call
@csrf_protect
def update_multiple(request):
    """Handles PUT requests to update multiple users with different data.
    Expected data:
        - fields: list of fields to update (allowed: firstName, lastName, email, role_id)
        - users: list of user dicts containing 'id' and corresponding field values to update


    Users.objects.filter(
        id__in=[1, 2, 3]
    ).update(
        firstName=Case(
            When(id=1, then=Value("Rahul")),
            When(id=2, then=Value("Jay")),
            When(id=3, then=Value("Amit")),
            output_field=CharField()
        ),

        lastName=Case(
            When(id=1, then=Value("Patel")),
            When(id=2, then=Value("Shah")),
            When(id=3, then=Value("Mehta")),
            output_field=CharField()
        )
    )



    """

    if request.method != "PUT":
        return JsonResponse(
            {"message": "Only PUT method is allowed"},
            status=405
        )
    try:
        data = json.loads(request.body)

        fields = data["fields"]
        users = data["users"]

        # Fields that client is allowed to update
        allowed_fields = [
            "firstName",
            "lastName",
            "email",
            "role_id"
        ]

        # Check requested fields
        for field in fields:
            if field not in allowed_fields:
                return JsonResponse(
                    {"error": f"Invalid field: {field}"},
                    status=400
                )

        user_ids = []

        # Create CASE statements for every field
        cases = {}

        for field in fields:
            cases[field] = []

        # Build CASE WHEN for every user
        for user in users:

            user_id = user["id"]
            user_ids.append(user_id)

            for field in fields:

                if field in user:

                    cases[field].append(
                        When(
                            id=user_id,
                            then=Value(user[field])
                        )
                    )

        # Prepare update data
        update_data = {}

        for field in fields:

            if cases[field]:

                update_data[field] = Case(
                    *cases[field],
                    output_field=CharField()
                )

        # ONE database UPDATE
        updated_count = Users.objects.filter(
            id__in=user_ids
        ).update(**update_data)

        return JsonResponse({
            "message": "Users updated successfully",
            "updated_users": updated_count,
            "fields": fields
        })

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=400
        )




#User Login API
@csrf_protect
def login(request):
    """Handles POST requests to log in a user.
    Expected data: username, password"""
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            user = authenticate(request,username=data["username"], password=data["password"])
            if user:
                auth_login(request, user)
                return JsonResponse(
                    {"message": "User logged in successfully",
                    "user_id" : user.id,
                    "csrf_token" : request.META.get("CSRF_COOKIE")
                    },
                    status=200
                )
            else:
                return JsonResponse(
                    {"message": "Invalid credentials"},
                    status=401
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

def logout(request):
    """Handles POST requests to log out a user."""
    try:
        if request.method == "POST":
            logout(request)
            return JsonResponse(
                {"message": "User logged out successfully"},
                status=200
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

#Sign up API
@csrf_protect
def signup(request):
    """Handles POST requests to sign up a new user.
    Expected data: username, firstName, lastName, email, password, role"""
    if request.method == "POST":

        if Users.objects.filter(username=request.POST.get("username")).exists():
            return JsonResponse(
                {"message": "Username already exists"},
                status=400
            )
        
        if Users.objects.filter(email=request.POST.get("email")).exists():
            return JsonResponse(
                {"message": "Email already exists"},
                status=400
            )

        try:
            data = json.loads(request.body)

            user = Users.objects.create_user(
                username = data["username"],
                email = data["email"],
                firstName = data["firstName"],
                lastName = data["lastName"],
                role_id = data["role"]
            )

            user.set_password(data["password"])

            user.save()

            if user:
                auth_login(request, user)
                return JsonResponse(
                    {
                    "message": "User created successfully",
                    "user_id" : user.id,
                    "csrf_token" : request.META.get("CSRF_COOKIE")
                },
                status=200
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

        

