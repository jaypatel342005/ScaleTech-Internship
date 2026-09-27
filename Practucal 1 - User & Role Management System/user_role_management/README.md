# 👥 User & Role Management System

A RESTful API backend built with **Django** that provides complete user and role management capabilities. The system supports user authentication, role-based access control (RBAC), CRUD operations, bulk updates, module-level access checking, and comes with a built-in **Swagger UI** for interactive API exploration.

---

## 📋 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack & Dependencies](#tech-stack--dependencies)
- [Python Version](#python-version)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Running the Project Locally](#running-the-project-locally)
- [Database](#database)
- [Authentication & CSRF](#authentication--csrf)

---

## Introduction

The **User & Role Management System** is a Django-based backend API that enables complete management of users and their assigned roles. Each user can be assigned a role, and each role defines a set of **access modules** (e.g., `dashboard`, `reports`, `settings`). The system allows you to:

- Register, authenticate, and manage users
- Define roles with specific module-level permissions
- Check whether a logged-in user has access to a particular module
- Perform bulk updates on multiple users in a single optimized database call
- Explore all APIs interactively via the built-in Swagger UI

---

## ✨ Features

### User Management
- ✅ Create, Read, Update, Delete (CRUD) users
- ✅ User sign-up with automatic login
- ✅ Session-based login and logout
- ✅ Update a single user or multiple users at once (same or different data)
- ✅ Bulk update multiple users with different field values in **one** database query (using Django `Case/When`)
- ✅ Search users by `username`, `firstName`, `lastName`, `email`, or `role_id`
- ✅ Module-level access check for authenticated users
- ✅ CSRF-protected write endpoints

### Role Management
- ✅ Create, Read, Update, Delete (CRUD) roles
- ✅ Manage `accessModules` — add or remove module permissions from a role
- ✅ Unique role names enforced at the database level
- ✅ Active/Inactive status for roles
- ✅ Search roles by `roleName`, `accessModules`, or `active` status

### Developer Experience
- ✅ Built-in **Swagger UI** served at the root URL (`/`)
- ✅ Raw **OpenAPI 3.0 JSON spec** available at `/api/schema.json`
- ✅ Django Admin panel for direct database management

---

## 🛠 Tech Stack & Dependencies

| Package  | Version  | Purpose                          |
|----------|----------|----------------------------------|
| Django   | 6.1.1    | Web framework & ORM              |
| SQLite3  | Built-in | Default development database     |
| Python   | 3.10+    | Runtime language                 |

> All dependencies are listed in `requirements.txt`.

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🐍 Python Version

**Minimum Required: Python 3.10+**

This project uses:
- `django.db.models.JSONField` (requires Python 3.8+ & Django 3.1+)
- f-strings, type hints, and other modern Python features

Verify your Python version:
```bash
python --version
```

---

## 📁 Project Structure

```
user_role_management/               ← Project root
│
├── manage.py                       ← Django management entry point
├── requirements.txt                ← Project dependencies
├── db.sqlite3                      ← SQLite development database
│
├── user_role_management/           ← Core Django configuration package
│   ├── settings.py                 ← Project settings (DB, apps, middleware, etc.)
│   ├── urls.py                     ← Root URL dispatcher (routes to apps + Swagger)
│   ├── swagger_view.py             ← Renders the Swagger UI at the root URL
│   ├── openapi.py                  ← Full OpenAPI 3.0 specification (JSON)
│   ├── asgi.py                     ← ASGI server entry point
│   └── wsgi.py                     ← WSGI server entry point
│
├── users/                          ← Users app
│   ├── models.py                   ← Users model (extends Django built-in User)
│   ├── views.py                    ← All user-related API view functions
│   ├── urls.py                     ← URL routes for user endpoints
│   ├── admin.py                    ← Django admin registration for Users
│   ├── apps.py                     ← App configuration
│   ├── tests.py                    ← Test cases (placeholder)
│   └── migrations/                 ← Database migration files
│
└── roles/                          ← Roles app
    ├── models.py                   ← Role model (roleName, accessModules, active)
    ├── views.py                    ← All role-related API view functions
    ├── urls.py                     ← URL routes for role endpoints
    ├── access_urls.py              ← (Reserved) Access module URL definitions
    ├── admin.py                    ← Django admin registration for Roles
    ├── apps.py                     ← App configuration
    ├── tests.py                    ← Test cases (placeholder)
    └── migrations/                 ← Database migration files
```

### App Descriptions

#### `users/` — User Management App
Handles all user-related operations. The `Users` model extends Django's built-in `User` model with additional fields (`firstName`, `lastName`, `role`). Contains full CRUD APIs, authentication endpoints, bulk update logic using Django's `Case/When` ORM feature, and a module access-check endpoint.

#### `roles/` — Role Management App
Handles all role-related operations. The `Role` model stores a role name, a JSON list of accessible module names, a creation timestamp, and an active flag. Contains full CRUD APIs, access module management (add/remove), and search functionality.

#### `user_role_management/` — Core Configuration
The Django project settings package. Configures installed apps, middleware, database, URL routing, and hosts the Swagger UI and OpenAPI spec.

---

## 🔗 API Endpoints

### User Endpoints — `/api/user/`

| Method   | Endpoint                           | Description                                       |
|----------|------------------------------------|---------------------------------------------------|
| GET      | `/api/user/`                       | Retrieve all users with their roles               |
| POST     | `/api/user/create/`                | Create a new user (admin-style, requires CSRF)    |
| PUT      | `/api/user/update/<id>/`           | Update a single user by ID                        |
| DELETE   | `/api/user/delete/<username>/`     | Delete a user by username                         |
| POST     | `/api/user/signup/`                | Register a new user (auto-login on success)       |
| POST     | `/api/user/login/`                 | Log in with username and password                 |
| POST     | `/api/user/logout/`                | Log out the current session                       |
| PUT      | `/api/user/update-multiple/`       | Update multiple users with the same data          |
| PUT      | `/api/user/bulk-update/`           | Update multiple users with different data         |
| GET      | `/api/user/access-check/<module>/` | Check if logged-in user can access a module       |
| GET      | `/api/user/search/`                | Search users by field and value                   |
| GET      | `/api/user/csrf/`                  | Retrieve a CSRF token                             |

### Role Endpoints — `/api/role/`

| Method   | Endpoint                      | Description                                      |
|----------|-------------------------------|--------------------------------------------------|
| GET      | `/api/role/`                  | Retrieve all roles                               |
| POST     | `/api/role/create/`           | Create a new role                                |
| PUT      | `/api/role/update/<id>/`      | Update a role by ID                              |
| DELETE   | `/api/role/delete/<id>/`      | Delete a role by ID                              |
| PUT      | `/api/role/access/update/`    | Set/replace access modules for a role            |
| PUT      | `/api/role/access/remove/`    | Remove specific access modules from a role       |
| GET      | `/api/role/search/`           | Search roles by field and value                  |

### Other Endpoints

| Method | Endpoint           | Description                             |
|--------|--------------------|-----------------------------------------|
| GET    | `/`                | Swagger UI — interactive API docs       |
| GET    | `/api/schema.json` | Raw OpenAPI 3.0 JSON specification      |
| GET    | `/admin/`          | Django Admin panel                      |

---

## 🚀 Running the Project Locally

### Prerequisites

Make sure you have the following installed:
- Python 3.10 or higher
- `pip` (Python package installer)
- Git (optional, for cloning)

---

### Step 1 — Clone the Repository

```bash
git clone <your-repository-url>
cd "Practucal 1 - User & Role Management System/user_role_management"
```

---

### Step 2 — Create a Virtual Environment

It is strongly recommended to use a virtual environment to isolate project dependencies.

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt once activated.

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4 — Apply Database Migrations

Run Django migrations to create the required database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 5 — Create a Superuser (Optional)

To access the Django Admin panel at `/admin/`, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

---

### Step 6 — Start the Development Server

```bash
python manage.py runserver
```

The server will start at: **http://127.0.0.1:8000/**

| URL                              | Description                   |
|----------------------------------|-------------------------------|
| http://127.0.0.1:8000/           | Swagger UI (interactive docs) |
| http://127.0.0.1:8000/admin/     | Django Admin panel            |
| http://127.0.0.1:8000/api/user/  | User API                      |
| http://127.0.0.1:8000/api/role/  | Role API                      |

---

### Step 7 — Explore the API via Swagger UI

Open your browser and navigate to **http://127.0.0.1:8000/**. The Swagger UI loads automatically and lets you:
- Browse all available endpoints
- Read request/response schemas
- Send test requests directly from the browser

---

## 🗃 Database

The project uses **SQLite** as the default database, stored in `db.sqlite3` at the project root. This requires zero configuration and is ideal for development and internship demonstrations.

### Models

**`Role`** — `roles/models.py`

| Field         | Type          | Description                                |
|---------------|---------------|--------------------------------------------|
| id            | AutoField     | Primary key                                |
| roleName      | CharField     | Unique name for the role                   |
| accessModules | JSONField     | List of module names this role can access  |
| createdAt     | DateTimeField | Auto-set timestamp when role is created    |
| active        | BooleanField  | Whether the role is currently active       |

**`Users`** — `users/models.py` (extends Django's built-in `User`)

| Field     | Type       | Description                               |
|-----------|------------|-------------------------------------------|
| user_ptr  | OneToOne   | Link to Django's built-in auth User       |
| firstName | CharField  | User's first name                         |
| lastName  | CharField  | User's last name                          |
| role      | ForeignKey | Reference to the Role model (nullable)    |

> Django's built-in `User` already provides `username`, `email`, `password`, `is_staff`, `is_active`, etc.

---

## 🔐 Authentication & CSRF

This project uses **Django's session-based authentication**.

### Getting a CSRF Token

Before making any `POST`, `PUT`, or `DELETE` requests from a client:

1. Call `GET /api/user/csrf/` to receive a CSRF cookie
2. Include the `X-CSRFToken` header in subsequent write requests

### Login Flow

```
1. GET  /api/user/csrf/                    → Receive CSRF cookie
2. POST /api/user/login/                   → Authenticate (returns session cookie + CSRF token)
3. GET  /api/user/access-check/<module>/   → Check module access (requires session)
4. POST /api/user/logout/                  → End the session
```

---

## 📝 Notes

- **DEBUG mode** is enabled by default (`settings.py`). Do **not** deploy to production with `DEBUG = True`.
- The `SECRET_KEY` in `settings.py` is a development key — replace it with a secure random value in production.
- CSRF protection is enforced on all write endpoints (`@csrf_protect`). Always obtain a CSRF token before testing POST/PUT requests.
- The Swagger UI is served by a custom view (`swagger_view.py`) using a static `openapi.py` spec file.

---

*Built as part of the Scaletech Internship — Practical 1: User & Role Management System*
