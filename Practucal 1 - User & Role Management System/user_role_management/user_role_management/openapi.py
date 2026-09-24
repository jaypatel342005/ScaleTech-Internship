"""
OpenAPI 3.0 specification for the User & Role Management API.
Generated from user_role_management.postman_collection.json
"""

OPENAPI_SPEC = {
    "openapi": "3.0.3",
    "info": {
        "title": "User & Role Management API",
        "description": (
            "A Django REST API for managing users and roles with full CRUD support, "
            "authentication, bulk operations, access control, and search capabilities."
        ),
        "version": "1.0.0",
        "contact": {
            "name": "ScaleTech Internship"
        }
    },
    "servers": [
        {
            "url": "http://127.0.0.1:8000",
            "description": "Local Development Server"
        }
    ],
    "tags": [
        {
            "name": "Authentication",
            "description": "Login, logout, and signup endpoints"
        },
        {
            "name": "Users",
            "description": "User CRUD, bulk operations, search, and access check"
        },
        {
            "name": "Roles",
            "description": "Role CRUD, access module management, and search"
        }
    ],
    "paths": {
        # ─── AUTH ────────────────────────────────────────────────────────────
        "/api/user/login/": {
            "post": {
                "tags": ["Authentication"],
                "summary": "Login",
                "description": "Authenticates a user with username and password. Returns session cookie and CSRF token.",
                "operationId": "user_login",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": ["username", "password"],
                                "properties": {
                                    "username": {"type": "string", "example": "jay"},
                                    "password": {"type": "string", "example": "123456"}
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Login successful",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string", "example": "User logged in successfully"},
                                        "user_id": {"type": "integer", "example": 1},
                                        "csrf_token": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "401": {"description": "Invalid credentials"},
                    "400": {"description": "Bad request"}
                }
            }
        },
        "/api/user/logout/": {
            "post": {
                "tags": ["Authentication"],
                "summary": "Logout",
                "description": "Logs out the currently authenticated user.",
                "operationId": "user_logout",
                "parameters": [
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": True,
                        "schema": {"type": "string"},
                        "description": "CSRF token obtained from login response"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Logout successful",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string", "example": "User logged out successfully"}
                                    }
                                }
                            }
                        }
                    },
                    "405": {"description": "Method not allowed"}
                }
            }
        },
        "/api/user/signup/": {
            "post": {
                "tags": ["Authentication"],
                "summary": "Signup",
                "description": "Creates a new user account and logs them in automatically.",
                "operationId": "user_signup",
                "parameters": [
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": True,
                        "schema": {"type": "string"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": ["username", "email", "password", "firstName", "lastName", "role"],
                                "properties": {
                                    "username": {"type": "string", "example": "rahul1232"},
                                    "email": {"type": "string", "format": "email", "example": "rahul2@gmail.com"},
                                    "password": {"type": "string", "example": "Rahul@123"},
                                    "firstName": {"type": "string", "example": "Rahul"},
                                    "lastName": {"type": "string", "example": "Patel"},
                                    "role": {"type": "integer", "example": 1, "description": "Role ID"}
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "User created and logged in",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string"},
                                        "user_id": {"type": "integer"},
                                        "csrf_token": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "400": {"description": "Username/email already exists or bad data"}
                }
            }
        },

        # ─── USERS ───────────────────────────────────────────────────────────
        "/api/user/": {
            "get": {
                "tags": ["Users"],
                "summary": "List all users",
                "description": "Returns a list of all users with their assigned role.",
                "operationId": "user_list",
                "responses": {
                    "200": {
                        "description": "List of users",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {"type": "integer"},
                                            "username": {"type": "string"},
                                            "firstName": {"type": "string"},
                                            "lastName": {"type": "string"},
                                            "email": {"type": "string"},
                                            "role": {
                                                "nullable": True,
                                                "type": "object",
                                                "properties": {
                                                    "roleName": {"type": "string"},
                                                    "accessModules": {
                                                        "type": "array",
                                                        "items": {"type": "string"}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/api/user/create/": {
            "post": {
                "tags": ["Users"],
                "summary": "Create user",
                "description": "Creates a new user. Use this for admin-level user creation (does not auto-login).",
                "operationId": "user_create",
                "parameters": [
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": True,
                        "schema": {"type": "string"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": ["username", "email", "password", "firstName", "lastName"],
                                "properties": {
                                    "username": {"type": "string", "example": "rahul123"},
                                    "email": {"type": "string", "format": "email", "example": "rahul@gmail.com"},
                                    "password": {"type": "string", "example": "Rahul@123"},
                                    "firstName": {"type": "string", "example": "Rahul"},
                                    "lastName": {"type": "string", "example": "Patel"},
                                    "is_superuser": {"type": "boolean", "example": False},
                                    "is_staff": {"type": "boolean", "example": False},
                                    "is_active": {"type": "boolean", "example": True},
                                    "role_id": {
                                        "nullable": True,
                                        "type": "integer",
                                        "example": None,
                                        "description": "Foreign key to Role"
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "User created successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string", "example": "User created successfully"},
                                        "id": {"type": "integer"}
                                    }
                                }
                            }
                        }
                    },
                    "400": {"description": "Bad request"}
                }
            }
        },
        "/api/user/update/{id}/": {
            "put": {
                "tags": ["Users"],
                "summary": "Update user by ID",
                "description": "Updates a single user identified by their numeric ID.",
                "operationId": "user_update",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                        "example": 2
                    },
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": True,
                        "schema": {"type": "string"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "username": {"type": "string"},
                                    "firstName": {"type": "string"},
                                    "lastName": {"type": "string"},
                                    "email": {"type": "string", "format": "email"},
                                    "is_superuser": {"type": "boolean"},
                                    "is_staff": {"type": "boolean"},
                                    "role_id": {"nullable": True, "type": "integer"}
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "User updated successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "400": {"description": "Bad request"},
                    "405": {"description": "Method not allowed"}
                }
            }
        },
        "/api/user/delete/{username}/": {
            "delete": {
                "tags": ["Users"],
                "summary": "Delete user by username",
                "description": "Deletes a user identified by their username string.",
                "operationId": "user_delete",
                "parameters": [
                    {
                        "name": "username",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "string"},
                        "example": "jay"
                    },
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": True,
                        "schema": {"type": "string"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "User deleted successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "400": {"description": "Bad request"},
                    "405": {"description": "Method not allowed"}
                }
            }
        },
        "/api/user/update-multiple/": {
            "put": {
                "tags": ["Users"],
                "summary": "Update multiple users (same data)",
                "description": "Updates a set of users (by IDs) with identical field values in one query.",
                "operationId": "user_update_multiple",
                "parameters": [
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": True,
                        "schema": {"type": "string"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": ["ids", "data"],
                                "properties": {
                                    "ids": {
                                        "type": "array",
                                        "items": {"type": "integer"},
                                        "example": [1, 2, 3]
                                    },
                                    "data": {
                                        "type": "object",
                                        "description": "Fields to update on all matched users",
                                        "example": {"firstName": "Jay", "lastName": "Patel"}
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Users updated successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "400": {"description": "Bad request"},
                    "405": {"description": "Method not allowed"}
                }
            }
        },
        "/api/user/bulk-update/": {
            "put": {
                "tags": ["Users"],
                "summary": "Bulk update users (different data per user)",
                "description": (
                    "Updates multiple users with different values per user in a single SQL UPDATE "
                    "using CASE/WHEN expressions. Allowed fields: firstName, lastName, email, role_id."
                ),
                "operationId": "user_bulk_update",
                "parameters": [
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": True,
                        "schema": {"type": "string"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": ["fields", "users"],
                                "properties": {
                                    "fields": {
                                        "type": "array",
                                        "items": {"type": "string", "enum": ["firstName", "lastName", "email", "role_id"]},
                                        "example": ["firstName", "lastName", "email"]
                                    },
                                    "users": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "required": ["id"],
                                            "properties": {
                                                "id": {"type": "integer"},
                                                "firstName": {"type": "string"},
                                                "lastName": {"type": "string"},
                                                "email": {"type": "string", "format": "email"}
                                            }
                                        },
                                        "example": [
                                            {"id": 1, "firstName": "Rahul", "lastName": "Patel", "email": "rahul@gmail.com"},
                                            {"id": 2, "firstName": "Jay", "lastName": "Shah", "email": "jay@gmail.com"}
                                        ]
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Bulk update successful",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string"},
                                        "updated_users": {"type": "integer"},
                                        "fields": {"type": "array", "items": {"type": "string"}}
                                    }
                                }
                            }
                        }
                    },
                    "400": {"description": "Bad request / invalid field"}
                }
            }
        },
        "/api/user/access-check/{module}/": {
            "get": {
                "tags": ["Users"],
                "summary": "Access check",
                "description": "Checks whether the currently logged-in user has access to the specified module.",
                "operationId": "user_access_check",
                "parameters": [
                    {
                        "name": "module",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "string"},
                        "example": "reports",
                        "description": "Module name to check access for"
                    },
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": False,
                        "schema": {"type": "string"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Access granted",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string", "example": "Access granted"}
                                    }
                                }
                            }
                        }
                    },
                    "401": {"description": "User not authenticated"},
                    "403": {"description": "Access denied"},
                    "400": {"description": "Bad request"}
                }
            }
        },
        "/api/user/search/": {
            "get": {
                "tags": ["Users"],
                "summary": "Search users",
                "description": "Search users by a specific field and value.",
                "operationId": "user_search",
                "parameters": [
                    {
                        "name": "searchBy",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "enum": ["username", "firstName", "lastName", "email", "role_id"]
                        },
                        "example": "firstName"
                    },
                    {
                        "name": "searchValue",
                        "in": "query",
                        "required": True,
                        "schema": {"type": "string"},
                        "example": "Jay"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Search results",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "users": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "id": {"type": "integer"},
                                                    "username": {"type": "string"},
                                                    "firstName": {"type": "string"},
                                                    "lastName": {"type": "string"},
                                                    "email": {"type": "string"},
                                                    "role_id": {"nullable": True, "type": "integer"}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "400": {"description": "Invalid search field"}
                }
            }
        },

        # ─── ROLES ───────────────────────────────────────────────────────────
        "/api/role/": {
            "get": {
                "tags": ["Roles"],
                "summary": "List all roles",
                "description": "Returns all roles with their access modules.",
                "operationId": "role_list",
                "responses": {
                    "200": {
                        "description": "List of roles",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {"type": "integer"},
                                            "roleName": {"type": "string"},
                                            "accessModules": {
                                                "type": "array",
                                                "items": {"type": "string"}
                                            },
                                            "active": {"type": "boolean"},
                                            "createdAt": {"type": "string", "format": "date-time"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/api/role/create/": {
            "post": {
                "tags": ["Roles"],
                "summary": "Create role",
                "description": "Creates a new role with the given name and access modules.",
                "operationId": "role_create",
                "parameters": [
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": True,
                        "schema": {"type": "string"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": ["roleName", "accessModules"],
                                "properties": {
                                    "roleName": {"type": "string", "example": "Admin"},
                                    "accessModules": {
                                        "type": "array",
                                        "items": {"type": "string"},
                                        "example": ["users", "roles", "dashboard", "reports", "settings"]
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Role created successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "400": {"description": "Bad request"}
                }
            }
        },
        "/api/role/update/{id}/": {
            "put": {
                "tags": ["Roles"],
                "summary": "Update role by ID",
                "description": "Updates an existing role's name, access modules, and active status.",
                "operationId": "role_update",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                        "example": 7
                    },
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": True,
                        "schema": {"type": "string"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "roleName": {"type": "string", "example": "Manager"},
                                    "accessModules": {
                                        "type": "array",
                                        "items": {"type": "string"},
                                        "example": ["dashboard", "users", "reports"]
                                    },
                                    "active": {"type": "boolean", "example": True},
                                    "createdAt": {"type": "string", "format": "date-time"}
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Role updated successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "400": {"description": "Bad request"},
                    "405": {"description": "Method not allowed"}
                }
            }
        },
        "/api/role/delete/{id}/": {
            "delete": {
                "tags": ["Roles"],
                "summary": "Delete role by ID",
                "description": "Deletes a role identified by its numeric ID.",
                "operationId": "role_delete",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                        "example": 2
                    },
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": True,
                        "schema": {"type": "string"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Role deleted successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "400": {"description": "Bad request"},
                    "405": {"description": "Method not allowed"}
                }
            }
        },
        "/api/role/access/update/": {
            "put": {
                "tags": ["Roles"],
                "summary": "Update role access modules",
                "description": "Replaces the access modules list for a role with a new de-duplicated list.",
                "operationId": "role_access_update",
                "parameters": [
                    {
                        "name": "X-CSRFToken",
                        "in": "header",
                        "required": True,
                        "schema": {"type": "string"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": ["id", "accessModules"],
                                "properties": {
                                    "id": {"type": "integer", "example": 3},
                                    "accessModules": {
                                        "type": "array",
                                        "items": {"type": "string"},
                                        "example": ["dashboard", "reports", "profile"]
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Role updated successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "404": {"description": "Role not found"},
                    "400": {"description": "Bad request"}
                }
            }
        },
        "/api/role/access/remove/": {
            "put": {
                "tags": ["Roles"],
                "summary": "Remove role access modules",
                "description": "Removes specific access modules from a role's current module list.",
                "operationId": "role_access_remove",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": ["id", "accessModules"],
                                "properties": {
                                    "id": {"type": "integer", "example": 3},
                                    "accessModules": {
                                        "type": "array",
                                        "items": {"type": "string"},
                                        "example": ["reports"]
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Access modules removed successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "404": {"description": "Access module not found in role"},
                    "400": {"description": "Bad request"}
                }
            }
        },
        "/api/role/search/": {
            "get": {
                "tags": ["Roles"],
                "summary": "Search roles",
                "description": "Search roles by roleName, accessModules, or active status.",
                "operationId": "role_search",
                "parameters": [
                    {
                        "name": "searchBy",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "enum": ["roleName", "accessModules", "active"]
                        },
                        "example": "accessModules"
                    },
                    {
                        "name": "searchValue",
                        "in": "query",
                        "required": True,
                        "schema": {"type": "string"},
                        "example": "dashboard"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Search results",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "roles": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "id": {"type": "integer"},
                                                    "roleName": {"type": "string"},
                                                    "accessModules": {
                                                        "type": "array",
                                                        "items": {"type": "string"}
                                                    },
                                                    "active": {"type": "boolean"}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "400": {"description": "Invalid search field"}
                }
            }
        }
    }
}
