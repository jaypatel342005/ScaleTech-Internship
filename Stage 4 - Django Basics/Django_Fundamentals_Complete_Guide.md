# Django Fundamentals - Complete Internship Guide

> **Purpose:** Learning and Revision Reference for Python/Django Internship
> **Level:** Beginner to Practical Development to Interview Ready
> **Stage:** 4 - Django Basics

---

## Table of Contents

1. [What is Django?](#1-what-is-django)
2. [Installing Django](#2-installing-django)
3. [Virtual Environment Setup](#3-virtual-environment-setup)
4. [Create a Django Project](#4-create-a-django-project)
5. [Run the Django Server](#5-run-the-django-server)
6. [Project vs App](#6-project-vs-app)
7. [Django MVT Architecture](#7-django-mvt-architecture)
8. [manage.py Commands](#8-managepy-commands)
9. [settings.py Explained](#9-settingspy-explained)
10. [urls.py and URL Routing](#10-urlspy-and-url-routing)
11. [Function-Based Views (FBV)](#11-function-based-views-fbv)
12. [Class-Based Views (CBV)](#12-class-based-views-cbv)
13. [FBV vs CBV Comparison](#13-fbv-vs-cbv-comparison)
14. [Models](#14-models)
15. [Django ORM](#15-django-orm)
16. [Migrations](#16-migrations)
17. [Templates](#17-templates)
18. [Static Files](#18-static-files)
19. [Complete Mini Django Example](#19-complete-mini-django-example)
20. [Complete Request Flow](#20-complete-request-flow)
21. [Test Cases in Django](#21-test-cases-in-django)
22. [Django Admin](#22-django-admin)
23. [Important Security Concepts](#23-important-security-concepts)
24. [Quick Revision Summary](#24-quick-revision-summary)
25. [Interview Questions](#25-interview-questions)
26. [Learning Progression Roadmap](#26-learning-progression-roadmap)

---

## 1. What is Django?

**Django** is a high-level Python web framework used to build web applications and APIs.

It provides many things **out of the box**:

| Feature | Description |
|---|---|
| URL routing | Maps URLs to views |
| Database ORM | Interact with DB using Python |
| Authentication | Built-in user auth system |
| Admin panel | Auto-generated admin UI |
| Forms | Form handling and validation |
| Security | CSRF, XSS, SQL injection protection |
| Sessions | Session management |
| Middleware | Request/response processing layers |
| Testing | Built-in testing framework |
| Static files | CSS, JS, image handling |
| Template engine | Django Template Language (DTL) |

> **Key Concept:** Django handles the `request -> processing -> database -> response` flow for you.

### Applications You Can Build with Django

- E-commerce websites
- Student management systems
- Banking applications
- Blog systems
- Admin dashboards
- REST APIs
- AI/ML backend APIs
- Job portals
- Social media applications

---

## 2. Installing Django

### Step 1 - Check Python

```bash
python --version
# or
py --version
```

### Step 2 - Install Django (inside virtual env)

```bash
pip install django
```

### Step 3 - Verify Installation

```bash
django-admin --version
# or
python -m django --version
```

---

## 3. Virtual Environment Setup

Using a virtual environment keeps your project dependencies isolated.

### Create

```bash
cd "D:\College programming"
python -m venv django_env
```

This creates:
```
django_env/
    Scripts/
    Lib/
    Include/
```

### Activate (Windows)

```bash
django_env\Scripts\activate
```

You will see:
```
(django_env) D:\College programming>
```

### Deactivate

```bash
deactivate
```

---

## 4. Create a Django Project

```bash
django-admin startproject Basics
```

Generated structure:

```
Basics/                  <- project root
|
|-- manage.py
|
+-- Basics/              <- Django project package
    |-- __init__.py
    |-- settings.py
    |-- urls.py
    |-- asgi.py
    +-- wsgi.py
```

> NOTE: There are two folders named Basics. The outer is the project root, the inner is the actual Django package.

### Create an App

```bash
cd Basics
python manage.py startapp students
```

Generated app structure:

```
students/
    migrations/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

### Register the App in settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'students',   # <- Add your app here
]
```

---

## 5. Run the Django Server

```bash
python manage.py runserver
```

Output:
```
Starting development server at http://127.0.0.1:8000/
```

Open http://127.0.0.1:8000/ in your browser.

---

## 6. Project vs App

| Project | App |
|---|---|
| Complete website/application | Specific functionality module |
| Contains configuration | Contains feature logic |
| Can contain many apps | Belongs to a project |
| settings.py lives here | models.py, views.py, etc. live here |

### Example Structure

```
StudentManagement/         <- Project
|
|-- manage.py
|-- StudentManagement/
|   |-- settings.py
|   +-- urls.py
|
|-- students/              <- App
|-- teachers/              <- App
|-- courses/               <- App
|-- attendance/            <- App
+-- fees/                  <- App
```

---

## 7. Django MVT Architecture

> **MVT = Model + View + Template**

This is the **most important Django concept**.

```
Browser --> URLs --> View --> Template --> Browser (HTML)
                      |
                    Model
                      |
                   Database
```

### Model

- Responsible for database structure and operations
- Written in models.py

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

### View

- Receives requests, processes business logic, returns responses
- Written in views.py

```python
def home(request):
    return HttpResponse("Hello Django")
```

### Template

- HTML presentation layer with Django Template Language
- Lives in templates/ directory

```html
<h1>Welcome to Django</h1>
```

### MVC vs MVT Comparison

| MVC (Traditional) | MVT (Django) |
|---|---|
| Model | Model |
| Controller | View |
| View | Template |

> Django's View performs the role of MVC's Controller.
> Django's Template performs the role of MVC's View.

---

## 8. manage.py Commands

The command-line utility for all Django administrative tasks.

```bash
python manage.py <command>
```

### Complete Command Reference

| Command | Purpose |
|---|---|
| `runserver` | Start development server |
| `startapp <name>` | Create a new app |
| `makemigrations` | Generate migration files from model changes |
| `migrate` | Apply migrations to database |
| `createsuperuser` | Create an admin user |
| `shell` | Open Django interactive shell |
| `test` | Run test suite |
| `collectstatic` | Gather static files for production |
| `showmigrations` | List all migrations and their status |

```bash
python manage.py runserver
python manage.py startapp students
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell
python manage.py test
```

---

## 9. settings.py Explained

Contains the **complete configuration** of your Django project.

### SECRET_KEY

```python
SECRET_KEY = 'your-secret-key'
```

Used for: sessions, CSRF, signed data.

**Production:** Never expose it publicly. Use environment variables:

```python
import os
SECRET_KEY = os.environ.get("SECRET_KEY")
```

### DEBUG

```python
# Development
DEBUG = True

# Production - NEVER True in production!
DEBUG = False
```

When DEBUG=True, Django shows detailed error pages (file, line number, traceback).

### ALLOWED_HOSTS

```python
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]
```

### INSTALLED_APPS

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students',
]
```

### MIDDLEWARE

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]
```

Middleware sits between the client and Django:
```
Client -> Middleware -> Django App -> Middleware -> Client
```

Handles: security, session, CSRF, authentication.

### DATABASES

```python
# Default SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### ROOT_URLCONF

```python
ROOT_URLCONF = 'Basics.urls'
```

### STATIC_URL

```python
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # for production collectstatic
```

---

## 10. urls.py and URL Routing

### Basic URL

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),                    # matches /
    path('students/', views.student_list),   # matches /students/
]
```

### URL Parameters (Converters)

```python
path("student/<int:id>/", views.student_detail)   # Integer
path("student/<str:name>/", views.student)         # String
path("post/<slug:slug>/", views.post)               # Slug
path("record/<uuid:id>/", views.record)             # UUID
```

View usage:
```python
def student_detail(request, id):
    return HttpResponse(f"Student ID: {id}")
```

### Named URLs

```python
path("students/", views.students, name="students")
```

In templates - preferred over hardcoding:
```html
<a href="{% url 'students' %}">Students</a>
```

### URL Namespaces (for larger projects)

students/urls.py:
```python
app_name = "students"

urlpatterns = [
    path("", views.list_students, name="list"),
]
```

Template:
```html
{% url 'students:list' %}
```

### include() Pattern - Recommended for all projects

Project urls.py:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("students.urls")),
]
```

App students/urls.py:
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student-list"),
    path("<int:id>/", views.student_detail, name="student-detail"),
]
```

---

## 11. Function-Based Views (FBV)

A simple Python function that handles a request and returns a response.

```python
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello Django")
```

### FBV with HTTP Method Handling

```python
def student(request):
    if request.method == "GET":
        return HttpResponse("Getting students")
    elif request.method == "POST":
        return HttpResponse("Creating student")
```

### FBV with Template and Context

```python
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/list.html", {"students": students})
```

### FBV with URL Parameter

```python
def student_detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, "students/detail.html", {"student": student})
```

### When to Use FBV

- Simple logic
- Learning Django
- Custom non-standard behavior
- View does not fit standard CRUD patterns

---

## 12. Class-Based Views (CBV)

Using a class instead of a function:

```python
from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello Django")

    def post(self, request):
        return HttpResponse("POST request received")
```

URL registration:
```python
path("", HomeView.as_view())
```

> Note: as_view() converts the class into a callable view Django can use.

### Generic Class-Based Views

Django provides built-in generic CBVs:

```python
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
```

#### ListView Example

```python
from django.views.generic import ListView
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"
```

URL:
```python
path("students/", StudentListView.as_view(), name="student-list")
```

Django automatically fetches Student.objects.all() and passes as students.

#### CreateView Example

```python
from django.views.generic import CreateView
from django.urls import reverse_lazy

class StudentCreateView(CreateView):
    model = Student
    fields = ["name", "age", "email"]
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student-list")
```

### When to Use CBV

- CRUD operations
- Reusable patterns across views
- Larger applications
- When generic views save boilerplate

---

## 13. FBV vs CBV Comparison

| Aspect | FBV | CBV |
|---|---|---|
| Structure | Function | Class |
| Readability | Simple, explicit | More structured |
| Control | Direct | Abstracted |
| Reusability | Lower | Higher |
| Best for | Custom logic | CRUD operations |
| Learning curve | Beginner-friendly | More complex |
| Generic views | No | Yes (ListView, CreateView, etc.) |
| Method handling | if/elif request.method | Separate get(), post() methods |

> Rule: Choose the approach that makes the code clearer and easier to maintain.

---

## 14. Models

Models represent database tables as Python classes.

### Basic Model

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

Django auto-creates an `id` primary key unless you define one.

### Common Model Fields

| Field | Description | Example |
|---|---|---|
| `CharField` | Short text | `models.CharField(max_length=100)` |
| `TextField` | Long text | `models.TextField()` |
| `IntegerField` | Integer | `models.IntegerField()` |
| `DecimalField` | Decimal number | `models.DecimalField(max_digits=10, decimal_places=2)` |
| `BooleanField` | True/False | `models.BooleanField(default=False)` |
| `DateField` | Date only | `models.DateField()` |
| `DateTimeField` | Date + time | `models.DateTimeField(auto_now_add=True)` |
| `EmailField` | Email address | `models.EmailField()` |
| `URLField` | URL | `models.URLField()` |
| `FileField` | File upload | `models.FileField(upload_to='files/')` |
| `ImageField` | Image upload | `models.ImageField(upload_to='images/')` |
| `ForeignKey` | Many-to-one | `models.ForeignKey(Course, on_delete=models.CASCADE)` |
| `ManyToManyField` | Many-to-many | `models.ManyToManyField(Course)` |

### Field Options

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(default="")
    is_active = models.BooleanField(default=True)
    joined = models.DateTimeField(auto_now_add=True)  # set on create
    updated = models.DateTimeField(auto_now=True)     # set on every save
```

---

## 15. Django ORM

ORM = **Object Relational Mapper**

Write Python instead of SQL:
```python
# SQL: SELECT * FROM students;
Student.objects.all()
```

### Basic ORM Operations

```python
# Get all records
students = Student.objects.all()

# Get single record (raises DoesNotExist if not found)
student = Student.objects.get(id=1)

# Filter records
young = Student.objects.filter(age=20)

# Exclude records
others = Student.objects.exclude(age=20)

# Order by field
students = Student.objects.order_by('name')    # ascending
students = Student.objects.order_by('-name')   # descending

# Create record
student = Student.objects.create(
    name="Jay",
    age=21,
    email="jay@example.com"
)

# Update a record
student = Student.objects.get(id=1)
student.age = 22
student.save()

# Bulk update
Student.objects.filter(age=20).update(age=21)

# Delete a record
student = Student.objects.get(id=1)
student.delete()

# Count
count = Student.objects.count()

# Check if exists
exists = Student.objects.filter(name="Jay").exists()

# Get or create
student, created = Student.objects.get_or_create(
    email="jay@example.com",
    defaults={"name": "Jay", "age": 21}
)
```

### Field Lookups (Filters)

```python
Student.objects.filter(age=20)                    # exact match
Student.objects.filter(age__gt=18)               # greater than
Student.objects.filter(age__gte=18)              # greater than or equal
Student.objects.filter(age__lt=25)               # less than
Student.objects.filter(age__lte=25)              # less than or equal
Student.objects.filter(name__icontains="jay")    # case-insensitive contains
Student.objects.filter(name__startswith="J")     # starts with
Student.objects.filter(name__endswith="ay")      # ends with
Student.objects.filter(id__in=[1, 2, 3])         # in a list
```

---

## 16. Migrations

Migrations track and apply database schema changes over time.

### Workflow

```bash
# Step 1: After modifying models.py
python manage.py makemigrations

# Step 2: Apply changes to the database
python manage.py migrate
```

### Why Migrations?

Initial model:
```python
class Student(models.Model):
    name = models.CharField(max_length=100)
```

After adding a field:
```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()    # <- new field added
```

1. `makemigrations` generates: "Add age column to Student table."
2. `migrate` applies it to the actual database.

### Useful Migration Commands

```bash
python manage.py showmigrations                    # list all migrations
python manage.py sqlmigrate students 0001          # show SQL for a migration
python manage.py migrate students 0001             # migrate to specific version
python manage.py migrate students zero             # roll back all app migrations
```

---

## 17. Templates

### Configuration in settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # global templates folder
        'APP_DIRS': True,                   # also looks in app/templates/
    }
]
```

### Template Variables

View:
```python
def home(request):
    context = {
        "name": "Jay",
        "age": 21,
        "students": ["Rahul", "Amit", "Priya"]
    }
    return render(request, "home.html", context)
```

Template:
```html
<h1>Hello {{ name }}</h1>
<p>Age: {{ age }}</p>
```

### Template Tags

#### Conditions
```html
{% if age >= 18 %}
    <p>Adult</p>
{% elif age >= 13 %}
    <p>Teenager</p>
{% else %}
    <p>Child</p>
{% endif %}
```

#### Loops
```html
{% for student in students %}
    <li>{{ forloop.counter }}. {{ student.name }}</li>
{% empty %}
    <p>No students found.</p>
{% endfor %}
```

#### Comments
```html
{# This is a Django template comment - not shown in HTML #}
```

### Template Inheritance

base.html (the shared layout):
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">Home</a> |
        <a href="/students/">Students</a>
    </nav>

    <main>
        {% block content %}
        {% endblock %}
    </main>

    {% block scripts %}
    {% endblock %}
</body>
</html>
```

home.html (child template extending base):
```html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Welcome Home</h1>
    <p>This content replaces the block in base.html</p>
{% endblock %}
```

### Template Filters

```html
{{ name|upper }}             <!-- JAY -->
{{ name|lower }}             <!-- jay -->
{{ name|title }}             <!-- Jay Patel -->
{{ text|truncatewords:5 }}   <!-- First 5 words... -->
{{ items|length }}           <!-- count items in list -->
{{ date|date:"d M Y" }}      <!-- 16 Sep 2026 -->
{{ number|floatformat:2 }}   <!-- 3.14 -->
```

---

## 18. Static Files

Static files = CSS, JavaScript, Images, Fonts - assets that don't change per request.

### Recommended Structure

```
students/
    static/
        students/           <- namespace to avoid collisions
            css/
                style.css
            js/
                script.js
            images/
                logo.png
```

> Always use the app-name subfolder inside static/ to prevent collisions between apps.

### settings.py

```python
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # production collectstatic destination
```

### Using Static Files in Templates

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'students/css/style.css' %}">
</head>
<body>
    <img src="{% static 'students/images/logo.png' %}" alt="Logo">
    <script src="{% static 'students/js/script.js' %}"></script>
</body>
</html>
```

> Always use {% static %} tag - never hardcode /static/ paths.

### Static vs Media Files

| Static Files | Media Files |
|---|---|
| Developer-provided assets | User-uploaded files |
| CSS, JS, Icons, Fonts | Profile photos, PDFs, Documents |
| Deployed by developer | Uploaded at runtime by users |
| STATIC_URL / STATIC_ROOT | MEDIA_URL / MEDIA_ROOT |

### Production - Collect Static

```bash
python manage.py collectstatic
```

Gathers all static files from all apps into STATIC_ROOT for the web server.

---

## 19. Complete Mini Django Example

### Full File Structure

```
Basics/
|-- manage.py
|-- Basics/
|   |-- settings.py
|   +-- urls.py
+-- students/
    |-- migrations/
    |-- templates/
    |   +-- students/
    |       +-- list.html
    |-- static/
    |   +-- students/
    |       +-- css/style.css
    |-- admin.py
    |-- models.py
    |-- tests.py
    |-- urls.py
    +-- views.py
```

### models.py

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
```

```bash
python manage.py makemigrations
python manage.py migrate
```

### views.py

```python
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, "students/list.html", {"students": students})

def student_detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, "students/detail.html", {"student": student})
```

### students/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student-list"),
    path("<int:id>/", views.student_detail, name="student-detail"),
]
```

### Basics/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("students.urls")),
]
```

### templates/students/list.html

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Students</title>
    <link rel="stylesheet" href="{% static 'students/css/style.css' %}">
</head>
<body>
<h1>Student List</h1>

{% for student in students %}
    <div>
        <strong>{{ student.name }}</strong>
        - Age: {{ student.age }}
        - Email: {{ student.email }}
    </div>
{% empty %}
    <p>No students found.</p>
{% endfor %}

</body>
</html>
```

### admin.py

```python
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "email")
    search_fields = ("name", "email")
```

---

## 20. Complete Request Flow

**Scenario:** User visits `http://127.0.0.1:8000/students/5/`

```
Browser
   |
   |  GET /students/5/
   v
Django receives request
   |
   v
Basics/urls.py
   |  path("students/", include("students.urls"))  <- matches
   v
students/urls.py
   |  path("<int:id>/", views.student_detail)  <- matches, id=5
   v
student_detail(request, id=5) is called
   |
   |  student = Student.objects.get(id=5)
   v
Database query executes
   |
   |  Returns Student object with id=5
   v
render(request, "students/detail.html", {"student": student})
   |
   v
Template engine renders HTML
   |
   v
HttpResponse with HTML content
   |
   v
Browser displays the page
```

> INTERVIEW TIP: This flow is critically important. Practice explaining it verbally without notes.

---

## 21. Test Cases in Django

Django has a built-in testing framework based on Python's unittest module.

### Why Write Tests?

- Detect bugs early before they reach production
- Catch regressions when you change code
- Verify database behavior is correct
- Verify HTTP responses and status codes
- Verify correct templates are rendered
- Verify URL routing works correctly

### Run Tests

```bash
python manage.py test                              # run all tests
python manage.py test students                     # specific app
python manage.py test students.tests.StudentTest   # specific test class
python manage.py test -v 2                         # verbose output
```

### Basic Test

```python
from django.test import TestCase

class BasicTest(TestCase):
    def test_basic_math(self):
        self.assertEqual(2 + 3, 5)
```

### Test Models

```python
from django.test import TestCase
from .models import Student

class StudentModelTest(TestCase):

    def test_student_creation(self):
        student = Student.objects.create(
            name="Jay",
            age=21,
            email="jay@example.com"
        )
        self.assertEqual(student.name, "Jay")
        self.assertEqual(student.age, 21)

    def test_student_str_method(self):
        student = Student(name="Jay")
        self.assertEqual(str(student), "Jay")

    def test_student_email_unique(self):
        Student.objects.create(name="Jay", age=21, email="jay@example.com")
        count = Student.objects.filter(email="jay@example.com").count()
        self.assertEqual(count, 1)
```

### Test Views

```python
from django.test import TestCase

class HomeViewTest(TestCase):

    def test_home_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_template_used(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")
```

### Test with Database Data in Views

```python
from django.test import TestCase
from .models import Student

class StudentViewTest(TestCase):

    def test_student_list_page(self):
        Student.objects.create(name="Jay", age=21, email="jay@example.com")
        Student.objects.create(name="Rahul", age=22, email="rahul@example.com")

        response = self.client.get("/students/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "students/list.html")
        self.assertContains(response, "Jay")
        self.assertContains(response, "Rahul")

    def test_student_detail_page(self):
        student = Student.objects.create(name="Jay", age=21, email="jay@example.com")
        response = self.client.get(f"/students/{student.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jay")
```

### setUp() and tearDown()

```python
class StudentTest(TestCase):

    def setUp(self):
        # Runs BEFORE each test method
        self.student = Student.objects.create(
            name="Jay",
            age=21,
            email="jay@example.com"
        )

    def tearDown(self):
        # Runs AFTER each test method
        # Django automatically handles DB cleanup for TestCase
        pass

    def test_student_name(self):
        self.assertEqual(self.student.name, "Jay")

    def test_student_age(self):
        self.assertEqual(self.student.age, 21)
```

### Common Assertions Reference

| Assertion | Checks |
|---|---|
| `assertEqual(a, b)` | a == b |
| `assertNotEqual(a, b)` | a != b |
| `assertTrue(x)` | x is True |
| `assertFalse(x)` | x is False |
| `assertIsNone(x)` | x is None |
| `assertIn(a, b)` | a in b |
| `assertContains(response, text)` | Response body contains text |
| `assertNotContains(response, text)` | Response body does not contain text |
| `assertTemplateUsed(response, name)` | Template was used in render |
| `assertEqual(response.status_code, 200)` | HTTP 200 OK |

### HTTP Status Codes

| Code | Meaning |
|---|---|
| `200` | OK - Success |
| `201` | Created |
| `301` | Moved Permanently |
| `302` | Found (Redirect) |
| `400` | Bad Request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Not Found |
| `500` | Internal Server Error |

### Test Categories

| Type | What it tests | Example |
|---|---|---|
| **Unit Test** | Small isolated pieces of logic | `assertEqual(func(input), expected)` |
| **Integration Test** | Multiple components working together | View -> Model -> Database -> Template |
| **Functional Test** | User-facing behavior end-to-end | Submit form -> redirect -> success page |

> Django creates a **separate test database** - your development data is never affected by tests.

---

## 22. Django Admin

Django provides a powerful built-in admin interface with zero configuration.

### Setup

```bash
python manage.py createsuperuser
```

Enter: username, email, password

### Access

Open: `http://127.0.0.1:8000/admin/`

### Register Models

```python
# students/admin.py
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

### Customize Admin Display

```python
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "email", "created_at")
    search_fields = ("name", "email")
    list_filter = ("age",)
    ordering = ("name",)
    readonly_fields = ("created_at",)
```

---

## 23. Important Security Concepts

### CSRF - Cross-Site Request Forgery

Always add `{% csrf_token %}` in every POST form:

```html
<form method="POST" action="/students/create/">
    {% csrf_token %}

    <input type="text" name="name">
    <button type="submit">Save</button>
</form>
```

Without this, Django will reject the form submission with a 403 error.

### SQL Injection Protection

Use Django ORM - it handles SQL escaping automatically:
```python
# SAFE - ORM parameterizes the query
Student.objects.filter(name=name)

# DANGEROUS - never do this
query = "SELECT * FROM students WHERE name = '" + name + "'"
```

### XSS - Cross-Site Scripting

Django templates auto-escape output by default:
```html
{{ user_input }}         <!-- auto-escaped (safe) -->
{{ user_input|safe }}    <!-- bypass escaping - use ONLY if truly safe -->
```

### render() vs HttpResponse() vs redirect()

```python
# Return a simple string
return HttpResponse("Hello")

# Render a template with context (most common for web pages)
return render(request, "home.html", {"name": "Jay"})

# Redirect to another URL (after POST-redirect-GET pattern)
from django.shortcuts import redirect
return redirect("student-list")    # by named URL
return redirect("/students/")      # by URL path
```

### POST-Redirect-GET Pattern

```python
def create_student(request):
    if request.method == "POST":
        # Save data
        Student.objects.create(
            name=request.POST["name"],
            age=request.POST["age"]
        )
        return redirect("student-list")  # prevents duplicate submissions

    return render(request, "students/form.html")
```

---

## 24. Quick Revision Summary

| Concept | One-liner |
|---|---|
| **Django** | High-level Python web framework |
| **Project** | Complete application with configuration |
| **App** | Modular component responsible for one feature |
| **MVT** | Model (DB) + View (Logic) + Template (UI) |
| **manage.py** | CLI for running all Django commands |
| **settings.py** | Project-wide configuration file |
| **urls.py** | Maps URL patterns to view functions/classes |
| **models.py** | Defines database tables as Python classes |
| **views.py** | Handles requests and returns responses |
| **Templates** | HTML + Django Template Language (DTL) |
| **Static files** | CSS, JS, Images - developer-provided assets |
| **Media files** | User-uploaded files at runtime |
| **ORM** | Query database with Python, not raw SQL |
| **Migrations** | Track and apply database schema changes |
| **FBV** | Function-Based View - plain Python function |
| **CBV** | Class-Based View - structured Python class |
| **Generic CBV** | ListView, CreateView, UpdateView, DeleteView |
| **TestCase** | Django base class for writing automated tests |
| **CSRF** | Cross-Site Request Forgery token in forms |
| **Django Admin** | Auto-generated admin panel at /admin/ |
| **include()** | Delegates URL patterns to app-level urls.py |
| **render()** | Renders template with context, returns response |
| **redirect()** | Sends browser to another URL |

---

## 25. Interview Questions

### Beginner Level

**Q1. What is Django?**

Django is a high-level Python web framework that provides URL routing, ORM, authentication, admin panel, and many built-in features out of the box, allowing developers to build secure, scalable, and maintainable web applications quickly without writing everything from scratch.

---

**Q2. What is MVT architecture?**

MVT stands for Model-View-Template:
- **Model** manages database structure and operations (models.py)
- **View** handles request/response logic and business logic (views.py)
- **Template** handles HTML presentation (templates/)

It is similar to MVC but Django's View acts as the Controller, and Django's Template acts as the traditional View.

---

**Q3. What is the difference between a project and an app?**

A **project** is the complete Django application containing global configuration (settings.py, main urls.py, wsgi.py). An **app** is a self-contained modular component within the project that handles a specific functionality — for example, students, authentication, or payments. One project can contain multiple apps.

---

**Q4. What is manage.py?**

manage.py is a command-line utility used to perform Django administrative tasks such as running the development server (runserver), creating apps (startapp), creating and applying database migrations (makemigrations, migrate), creating a superuser, and running tests.

---

**Q5. What is settings.py?**

settings.py contains all project-level configuration: SECRET_KEY, DEBUG mode, ALLOWED_HOSTS, INSTALLED_APPS, MIDDLEWARE, DATABASES connection settings, TEMPLATES configuration, STATIC_URL, and more.

---

### Intermediate Level

**Q6. What is Django ORM?**

Django ORM (Object Relational Mapper) is an abstraction layer that allows developers to interact with databases using Python objects and querysets instead of writing raw SQL. For example, Student.objects.all() instead of "SELECT * FROM students".

---

**Q7. What are migrations and why are they needed?**

Migrations are Django's mechanism for tracking changes to models and applying those changes to the database schema automatically. makemigrations generates migration files describing what changed, and migrate applies them to the actual database. This allows schema changes to be version-controlled and shared across teams.

---

**Q8. FBV vs CBV - when would you use each?**

**FBV** (Function-Based Views): Use for simple logic, custom non-standard behavior, or when learning. They are explicit and easy to understand.

**CBV** (Class-Based Views): Use for CRUD operations, when you want to reuse behavior across views, or when using Django's generic views (ListView, CreateView, UpdateView, DeleteView) which save significant boilerplate code.

---

**Q9. What are static files vs media files?**

**Static files** are developer-provided assets (CSS, JavaScript, icons, fonts) that are part of the application. They are served from STATIC_URL and collected with collectstatic for production.

**Media files** are user-uploaded files (profile photos, PDF documents, product images) uploaded at runtime. They are served from MEDIA_URL and stored at MEDIA_ROOT.

---

**Q10. What does include() do in Django URLs?**

include() allows delegating URL patterns to app-level urls.py files, keeping the project's main urls.py clean and organized. For example, path("students/", include("students.urls")) sends all requests starting with /students/ to the students app's urls.py for further routing.

---

### Testing Level

**Q11. How do you run Django tests?**

```bash
python manage.py test
```

**Q12. What is TestCase in Django?**

django.test.TestCase is Django's base test class that provides a test client (to simulate HTTP requests), database isolation (uses transactions rolled back after each test so tests don't affect each other), and Django-specific assertion helpers like assertContains and assertTemplateUsed.

---

**Q13. How do you test a view in Django?**

```python
def test_student_list(self):
    Student.objects.create(name="Jay", age=21, email="jay@example.com")
    response = self.client.get("/students/")
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "students/list.html")
    self.assertContains(response, "Jay")
```

---

**Q14. What is setUp() in Django tests?**

setUp() is a special method that runs automatically before each test method in a TestCase. It is used to create shared test data or initialize objects needed across multiple test methods, avoiding code duplication.

---

**Q15. What is CSRF protection in Django?**

CSRF (Cross-Site Request Forgery) is an attack where a malicious website tricks a logged-in user's browser into making unwanted requests to your app. Django protects against this with CsrfViewMiddleware, which generates a unique token for each session. Every POST form must include {% csrf_token %}, otherwise Django rejects the request with a 403 Forbidden error.

---

## 26. Learning Progression Roadmap

```
Python Basics
    |
    v
Django Installation and Setup
    |
    v
Project + App Structure
    |
    v
MVT Architecture (Model, View, Template)
    |
    v
URL Routing (path, include, named URLs)
    |
    v
Function-Based Views (FBV)
    |
    v
Templates and Template Inheritance
    |
    v
Models and ORM Basics
    |
    v
Migrations (makemigrations, migrate)
    |
    v
Class-Based Views (CBV + Generic Views)
    |
    v
Forms (Form, ModelForm, FormView)
    |
    v
CRUD Operations (Create, Read, Update, Delete)
    |
    v
Authentication (Login, Logout, Register, Permissions)
    |
    v
Static and Media Files
    |
    v
Testing (Unit Tests + Integration Tests)
    |
    v
Django REST Framework (DRF)
    |
    v
APIs (Serializers, ViewSets, Routers, Authentication)
    |
    v
Deployment (Gunicorn, Nginx, PostgreSQL, Environment Variables)
```

### Practice Project - Student Management System

Build this from scratch WITHOUT tutorials to validate your understanding:

```
Features to implement:
  - Add a new student (Create)
  - View all students list (Read)
  - View individual student details (Read)
  - Edit/update student information (Update)
  - Delete a student (Delete)
  - Search students by name

Tech stack to use:
  - Django MVT architecture
  - Models with ORM
  - ModelForms for validation
  - Templates with base.html inheritance
  - Static files for CSS styling
  - Named URL routing
  - Django Admin panel
  - At least 5 test cases
```

> Once you can build this from scratch WITHOUT looking at tutorials or notes, you have a solid Django fundamentals foundation ready for internship-level work.

---

## 27. Advanced URL Routing

### Query Parameters

URL with query string: `/students/?name=Jay&age=21`

The part after `?` is the **query string** — not defined in `path()`.

```python
def students(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    return HttpResponse(f"Name: {name}, Age: {age}")
```

Common uses: Search, Filtering, Sorting, Pagination.

### Path Parameter vs Query Parameter

| Type | Example | Used For |
|---|---|---|
| Path parameter | `/student/10/` | Identifying a specific resource |
| Query parameter | `/students/?age=21` | Filtering or modifying the request |

### `reverse()` — Generating URLs in Python

```python
from django.urls import reverse

url = reverse("student-list")           # returns /students/
url = reverse("student-detail", args=[5])  # returns /students/5/
```

Use instead of hardcoding `/students/` in Python code.

### URL Pattern Order Matters

Django checks URL patterns **in order**. Put specific patterns before generic ones:

```python
urlpatterns = [
    path("student/all/", views.all_students),     # specific first
    path("student/<int:id>/", views.student),     # generic after
]
```

### Custom URL Converter

```python
# converters.py
class FourDigitYearConverter:
    regex = '[0-9]{4}'
    def to_python(self, value):
        return int(value)
    def to_url(self, value):
        return '%04d' % value
```

```python
from django.urls import register_converter
register_converter(FourDigitYearConverter, 'yyyy')
path('articles/<yyyy:year>/', views.year_archive)
```

---

## 28. Advanced Static Files

### STATICFILES_DIRS

```python
# settings.py - add a global static folder
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

### STATICFILES_FINDERS

Django uses finders to locate static files:
```python
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
```

### Serving Static Files in Development

```python
# project/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your URLs
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### Media Files Configuration

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

```python
# project/urls.py
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Model with file upload:
```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='students/photos/', blank=True)
```

---

## 29. Advanced Testing

### Testing URLs with `reverse()`

```python
from django.urls import reverse

def test_student_list_url(self):
    url = reverse("student-list")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
```

Better than hardcoding `/students/` — URL changes won't break your tests.

### Testing POST Requests

```python
def test_create_student(self):
    response = self.client.post(
        reverse("student-create"),
        {"name": "Jay", "age": 21, "email": "jay@example.com"}
    )
    self.assertEqual(response.status_code, 302)  # redirect after success
    self.assertEqual(Student.objects.count(), 1)
```

### Testing Redirects

```python
def test_redirect_after_create(self):
    response = self.client.post(
        reverse("student-create"),
        {"name": "Jay", "age": 21, "email": "jay@example.com"}
    )
    self.assertRedirects(response, reverse("student-list"))
```

### Testing Context Data

```python
def test_context_contains_students(self):
    Student.objects.create(name="Jay", age=21, email="jay@example.com")
    response = self.client.get(reverse("student-list"))
    self.assertIn("students", response.context)
    self.assertEqual(len(response.context["students"]), 1)
```

### Testing Database Count Changes

```python
def test_student_deleted(self):
    student = Student.objects.create(name="Jay", age=21, email="jay@example.com")
    self.assertEqual(Student.objects.count(), 1)

    self.client.post(reverse("student-delete", args=[student.id]))
    self.assertEqual(Student.objects.count(), 0)
```

### Testing Authenticated Views

```python
from django.contrib.auth.models import User

class AuthenticatedViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="jay",
            password="testpass123"
        )
        self.client.login(username="jay", password="testpass123")

    def test_dashboard_authenticated(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)  # redirect to login
```

### Testing Forms

```python
from .forms import StudentForm

class StudentFormTest(TestCase):

    def test_valid_form(self):
        form = StudentForm(data={"name": "Jay", "age": 21, "email": "jay@example.com"})
        self.assertTrue(form.is_valid())

    def test_invalid_age(self):
        form = StudentForm(data={"name": "Jay", "age": 10, "email": "jay@example.com"})
        self.assertFalse(form.is_valid())
        self.assertIn("age", form.errors)

    def test_missing_required_field(self):
        form = StudentForm(data={"name": "", "age": 21, "email": "jay@example.com"})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
```

---

## 30. Advanced Database / ORM

### QuerySet Chaining

```python
students = (
    Student.objects
    .filter(age__gte=18)
    .exclude(name="Jay")
    .order_by("name")
    .select_related("department")
)
```

### QuerySet Lazy Evaluation

QuerySets are **lazy** — the database query is not executed until the data is actually needed:

```python
students = Student.objects.filter(age=21)   # no DB hit yet
for s in students:                           # DB hit happens here
    print(s.name)
```

This allows Django to build efficient queries before execution.

### `.first()` and `.last()`

```python
student = Student.objects.filter(age=21).first()   # returns object or None
student = Student.objects.all().last()
```

Safer than `.get()` when zero results are possible (`.get()` raises `DoesNotExist`).

### `.values()` and `.values_list()`

```python
# Returns list of dicts — lightweight
Student.objects.values("id", "name")
# [{"id": 1, "name": "Jay"}, ...]

# Returns list of tuples
Student.objects.values_list("name", flat=True)
# ['Jay', 'Rahul', 'Amit']
```

### Q Objects — OR and AND Queries

```python
from django.db.models import Q

# OR condition
Student.objects.filter(Q(age=18) | Q(age=21))

# AND condition (same as using multiple filter args)
Student.objects.filter(Q(age=21) & Q(name="Jay"))

# NOT condition
Student.objects.filter(~Q(age=21))
```

### F() Expressions — Database-level Field Operations

```python
from django.db.models import F

# Increment age by 1 directly in DB (efficient)
Student.objects.update(age=F('age') + 1)

# Compare two fields
Product.objects.filter(sale_price__lt=F('original_price'))
```

### Aggregation

```python
from django.db.models import Count, Avg, Sum, Max, Min

# Average age
Student.objects.aggregate(avg_age=Avg("age"))
# {'avg_age': 21.5}

# Count students
Student.objects.aggregate(total=Count("id"))

# Max and min age
Student.objects.aggregate(oldest=Max("age"), youngest=Min("age"))
```

### Annotation — Add Calculated Field to Each Object

```python
from django.db.models import Count

# Add employee_count to each department object
departments = Department.objects.annotate(
    employee_count=Count("employees")
)

for dept in departments:
    print(dept.name, dept.employee_count)
```

### select_related() — Avoid N+1 for ForeignKey

```python
# Without: hits DB for every department access in the loop (N+1 problem)
employees = Employee.objects.all()
for emp in employees:
    print(emp.department.name)   # extra query each time!

# With select_related: single JOIN query
employees = Employee.objects.select_related("department")
for emp in employees:
    print(emp.department.name)   # no extra queries
```

> Use `select_related` for `ForeignKey` and `OneToOneField`.

### prefetch_related() — Avoid N+1 for ManyToMany

```python
# Without: N+1 problem for many-to-many
students = Student.objects.all()
for s in students:
    print(s.courses.all())   # extra query each time!

# With prefetch_related: 2 optimized queries
students = Student.objects.prefetch_related("courses")
for s in students:
    print(s.courses.all())   # uses cached result
```

> Use `prefetch_related` for `ManyToManyField` and reverse relations.

### Custom Manager

```python
class ActiveStudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Student(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()         # default manager
    active = ActiveStudentManager()    # custom manager

# Usage
Student.active.all()         # only active students
Student.objects.all()        # all students
```

### Transactions

```python
from django.db import transaction

with transaction.atomic():
    # If any exception occurs, ALL DB changes inside are rolled back
    order = Order.objects.create(...)
    Stock.objects.filter(id=1).update(quantity=F('quantity') - 1)
    Payment.objects.create(...)
```

### `get_or_create()`

```python
student, created = Student.objects.get_or_create(
    email="jay@example.com",
    defaults={"name": "Jay", "age": 21}
)
# created = True if new, False if already existed
```

### `update_or_create()`

```python
student, created = Student.objects.update_or_create(
    email="jay@example.com",
    defaults={"name": "Jay Updated", "age": 22}
)
```

---

## 31. Model Relationships (Deep Dive)

### One-to-One

```python
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
```

Access:
```python
user.profile         # from user to profile
profile.user         # from profile to user
```

### Many-to-One (ForeignKey)

```python
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="employees"    # reverse access name
    )
```

Access:
```python
emp.department.name          # forward: employee -> department
dept.employees.all()         # reverse: department -> all employees
```

### Many-to-Many

```python
class Course(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name="students")
```

Operations:
```python
jay.courses.add(python, django)      # enroll
jay.courses.remove(python)           # unenroll
jay.courses.clear()                  # remove all
jay.courses.all()                    # get all courses

python.students.all()                # all students in python (reverse)
```

### on_delete Options

| Option | Behavior |
|---|---|
| `CASCADE` | Delete child when parent is deleted |
| `PROTECT` | Prevent parent deletion if children exist |
| `SET_NULL` | Set FK to NULL when parent is deleted (requires `null=True`) |
| `SET_DEFAULT` | Set FK to default value |
| `DO_NOTHING` | Do nothing (database may raise an error) |

### Cross-Relationship Filtering

```python
# Students in "IT" department
Student.objects.filter(department__name="IT")

# Students enrolled in "Django" course
Student.objects.filter(courses__name="Django")

# Departments that have at least one student over 20
Department.objects.filter(students__age__gt=20).distinct()
```

---

## 32. Model Methods and Properties

```python
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    fee_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2, default=10000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        # Method - called with student.is_adult()
        return self.age >= 18

    @property
    def full_name(self):
        # Property - accessed like an attribute: student.full_name
        return f"{self.first_name} {self.last_name}"

    @property
    def fee_balance(self):
        return self.total_fee - self.fee_paid

    class Meta:
        ordering = ['first_name']        # default ordering
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        db_table = 'students'            # custom DB table name
```

> **Method vs Property:** Use `@property` when the result behaves like an attribute (no side effects). Use a regular method when it takes arguments or has side effects.

> **Important:** Model methods do NOT create database columns. They are Python logic only.

---

## 33. Forms and Validations

### Why Django Forms?

Without Django Forms, you'd manually extract data from `request.POST`, manually validate each field, and manually handle errors. Django Forms provide a structured framework for all of this.

### Form Types

| Type | When to Use |
|---|---|
| `forms.Form` | Form not directly tied to a model |
| `forms.ModelForm` | Form directly tied to a Django model |

---

### forms.Form

```python
# forms.py
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18, max_value=100)
    course = forms.CharField(max_length=100)
```

### Common Form Fields

| Field | Validates |
|---|---|
| `CharField` | Text (with max_length) |
| `EmailField` | Valid email format |
| `IntegerField` | Integer (min_value, max_value) |
| `FloatField` | Float number |
| `BooleanField` | True/False (checkbox) |
| `ChoiceField` | Selection from choices list |
| `DateField` | Date format |
| `FileField` | File upload |
| `URLField` | Valid URL |

### Field Options

```python
name = forms.CharField(
    max_length=100,
    min_length=2,
    required=True,                # default is True
    label="Student Full Name",
    help_text="Enter your full name",
    initial="Jay",                # pre-filled default
    widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Your name"}
    )
)
```

### Widgets

```python
# Password input (hides text)
password = forms.CharField(widget=forms.PasswordInput())

# Textarea (multi-line text)
bio = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))

# Select dropdown
gender = forms.ChoiceField(
    choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
    widget=forms.Select(attrs={"class": "form-select"})
)

# Hidden input
token = forms.CharField(widget=forms.HiddenInput())
```

---

### forms.ModelForm

```python
# forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "course"]  # explicit is safer than '__all__'

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
        }

        labels = {
            "name": "Student Full Name",
        }

        help_texts = {
            "age": "Must be at least 18.",
        }
```

---

### Rendering Forms in Templates

```html
<form method="POST">
    {% csrf_token %}

    {{ form.as_p }}          <!-- wraps each field in <p> -->
    {# or: {{ form.as_table }} #}
    {# or: {{ form.as_ul }} #}

    <button type="submit">Submit</button>
</form>
```

Manual rendering (for custom styling):
```html
<form method="POST">
    {% csrf_token %}

    <div class="mb-3">
        <label for="{{ form.name.id_for_label }}">Name</label>
        {{ form.name }}
        {% for error in form.name.errors %}
            <div class="text-danger">{{ error }}</div>
        {% endfor %}
    </div>

    <button type="submit">Submit</button>
</form>
```

---

### Handling Form Submission in Views

```python
# views.py
from django.shortcuts import render, redirect
from .forms import StudentForm

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)        # bound form

        if form.is_valid():                     # runs validation
            form.save()                         # saves to DB (ModelForm)
            return redirect("student-list")     # PRG pattern

    else:
        form = StudentForm()                    # unbound form (empty)

    return render(request, "students/create.html", {"form": form})
```

> This GET/POST pattern is the **most important form view pattern in Django**. Memorize it.

---

### CSRF Protection

CSRF = Cross-Site Request Forgery — prevents malicious sites from making requests on behalf of your logged-in users.

```html
<form method="POST">
    {% csrf_token %}   <!-- generates hidden CSRF token -->
    ...
</form>
```

Without it, Django's `CsrfViewMiddleware` rejects POST with **403 Forbidden**.

**CSRF vs XSS:**
- **CSRF**: Attacker tricks your browser into making unwanted requests
- **XSS**: Attacker injects malicious JavaScript into a page

---

### Built-in Validation

```python
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "age"]

# Django automatically validates:
# - name: required, max 100 chars
# - email: valid email format
# - age: must be integer
```

---

### Custom Field Validation — `clean_<field>()`

```python
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "age"]

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 18:
            raise forms.ValidationError("Student must be at least 18 years old.")

        if age > 100:
            raise forms.ValidationError("Please enter a valid age.")

        return age    # always return the value

    def clean_email(self):
        email = self.cleaned_data["email"]

        # Normalize (clean the data)
        email = email.lower().strip()

        # Check uniqueness in DB
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")

        return email
```

---

### Multi-Field Validation — `clean()`

Used when validation depends on **multiple fields**:

```python
class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()                  # run field-level validation first

        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
```

### Validation Flow (Important for Interviews)

```
request.POST data
      |
      v
Form(request.POST)   <- bound form
      |
      v
form.is_valid()
      |
      v
  Field validation (type check, required, max_length, etc.)
      |
      v
  Field cleaning (each field's clean() method)
      |
      v
  clean_<field>() custom methods
      |
      v
  Form-wide clean() method
      |
      +----------+
      |          |
   INVALID     VALID
      |          |
  form.errors  form.cleaned_data
```

---

### clean_<field>() vs clean()

| Method | Purpose | When to Use |
|---|---|---|
| `clean_name()` | Validate one specific field | Field has its own validation rule |
| `clean_email()` | Validate one specific field | Field has its own validation rule |
| `clean()` | Validate multiple fields together | Passwords match, date range, etc. |

---

### `cleaned_data`

After `is_valid()` returns True:

```python
if form.is_valid():
    name = form.cleaned_data["name"]       # validated Python value
    email = form.cleaned_data["email"]
    age = form.cleaned_data["age"]

    # Do NOT use request.POST directly for validated data
```

---

### Custom Validators (Reusable)

```python
# validators.py
from django.core.exceptions import ValidationError
import re

def validate_no_spaces(value):
    if ' ' in value:
        raise ValidationError("Value cannot contain spaces.")

def validate_no_admin(value):
    if 'admin' in value.lower():
        raise ValidationError("This username is not allowed.")
```

Usage:
```python
from .validators import validate_no_spaces, validate_no_admin

class StudentForm(forms.Form):
    username = forms.CharField(
        validators=[validate_no_spaces, validate_no_admin]
    )
```

---

### ModelForm — Create vs Update

```python
# CREATE — new record
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student-list")
    else:
        form = StudentForm()
    return render(request, "students/form.html", {"form": form})


# UPDATE — existing record
def student_update(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)  # <- pass instance
        if form.is_valid():
            form.save()
            return redirect("student-list")
    else:
        form = StudentForm(instance=student)   # pre-populate with existing data
    return render(request, "students/form.html", {"form": form})
```

---

### `commit=False` — Modify Before Saving

```python
def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)   # create object but don't save yet
            todo.user = request.user          # add extra field not in form
            todo.save()                       # now save to DB
            return redirect("todo-list")
    else:
        form = TodoForm()
    return render(request, "todo/create.html", {"form": form})
```

---

### File Upload Forms

```python
# forms.py
class ResumeForm(forms.Form):
    name = forms.CharField()
    resume = forms.FileField()
```

```html
<!-- Template: enctype is REQUIRED for file uploads -->
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
```

```python
# views.py
def upload_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)  # <- include request.FILES
        if form.is_valid():
            uploaded_file = form.cleaned_data["resume"]
            print(uploaded_file.name)
    else:
        form = ResumeForm()
    return render(request, "upload.html", {"form": form})
```

---

### Non-Field Errors

```python
def clean(self):
    cleaned_data = super().clean()
    # This error is not tied to a specific field
    raise forms.ValidationError("Form-level error message.")
```

Template:
```html
{{ form.non_field_errors }}
```

Or with `add_error()`:
```python
self.add_error("email", "This email domain is not allowed.")
```

---

### Post/Redirect/Get (PRG) Pattern

```
POST /students/create/
         |
         v
   Save data
         |
         v
   redirect()       <-- never render on POST success
         |
         v
GET /students/
```

Without redirect, refreshing the browser after a POST can **re-submit the form** and create duplicate records.

---

### Forms Security Best Practices

| Rule | Reason |
|---|---|
| Always use `{% csrf_token %}` | Prevents CSRF attacks |
| Always validate server-side | Client-side can be bypassed |
| Use `form.cleaned_data` not `request.POST` | Gets clean, validated values |
| Use explicit `fields = [...]` in ModelForm | Never expose fields users shouldn't edit |
| Redirect after successful POST | PRG pattern — prevents duplicate submissions |
| Use DB constraints (`unique=True`) | Form validation alone is not enough under concurrency |
| Never store plaintext passwords | Use Django's `set_password()` |

---

### Forms Quick Revision

```
Forms
  |
  +-- forms.Form         (independent)
  |
  +-- forms.ModelForm    (tied to model)
        |
        +-- form.is_valid()     (run validation)
        |
        +-- form.cleaned_data   (validated values)
        |
        +-- form.save()         (save to DB)
        |
        +-- form.save(commit=False)  (modify before save)
        |
        +-- clean_<field>()     (per-field validation)
        |
        +-- clean()             (multi-field validation)
```

---

## 34. Forms Interview Questions

**Q1. Difference between Form and ModelForm?**

`forms.Form` creates a form independently of any model. `forms.ModelForm` automatically generates form fields from a model and can save validated data directly to the database with `.save()`.

**Q2. What does `is_valid()` do?**

It runs the complete validation pipeline: field type checking, required validation, `clean_<field>()` methods, and the form-level `clean()` method. Returns True if all pass, False otherwise.

**Q3. What is `cleaned_data`?**

A dictionary containing validated and cleaned form values, available after `is_valid()` returns True.

**Q4. Difference between `clean_<field>()` and `clean()`?**

`clean_<field>()` validates a single specific field. `clean()` is used for cross-field validation (e.g., comparing password and confirm_password).

**Q5. What is `commit=False`?**

`form.save(commit=False)` creates a model instance from the form data but does not save it to the database yet, allowing you to modify fields before calling `.save()`.

**Q6. What is CSRF and why use `{% csrf_token %}`?**

CSRF (Cross-Site Request Forgery) is an attack where a malicious site tricks a user's browser into making unwanted requests. `{% csrf_token %}` places a secret token in the form that Django validates on POST, rejecting requests without a valid token.

**Q7. What is the PRG pattern?**

Post/Redirect/Get: after a successful POST (form submission), redirect to a GET page instead of rendering a response directly. This prevents duplicate form submissions when the page is refreshed.

**Q8. Why use `fields = [...]` instead of `fields = '__all__'`?**

Explicitly listing fields prevents accidentally exposing sensitive model fields (like `is_admin`, `password`, `is_staff`) to user input.

---

## 35. Advanced ORM Interview Questions

**Q1. What is a QuerySet?**

A lazy, chainable representation of a database query. The actual SQL is not executed until the data is accessed (iteration, slicing, `list()`, `len()`, etc.).

**Q2. Difference between `filter()` and `get()`?**

`filter()` returns a QuerySet (zero or more results). `get()` returns exactly one object and raises `DoesNotExist` if none found or `MultipleObjectsReturned` if more than one.

**Q3. What is the N+1 problem?**

When you query a list of objects and then access a related object for each one in a loop, causing N additional queries. Solved with `select_related()` (for ForeignKey) or `prefetch_related()` (for ManyToMany).

**Q4. Difference between `select_related()` and `prefetch_related()`?**

`select_related()` uses SQL JOIN and is for `ForeignKey`/`OneToOneField`. `prefetch_related()` does separate queries and combines in Python — used for `ManyToManyField` and reverse relations.

**Q5. What are Q objects?**

`Q` objects allow complex queries with OR (`|`), AND (`&`), and NOT (`~`) operators that can't be expressed with simple `filter()` arguments.

**Q6. What is `transaction.atomic()`?**

A context manager that wraps database operations in a transaction. If any exception occurs inside the block, all database changes are rolled back.

**Q7. What is a custom Manager?**

A class that extends `models.Manager` to provide custom QuerySet methods. It encapsulates reusable database query logic in the model layer, keeping views clean.

**Q8. Difference between `annotate()` and `aggregate()`?**

`aggregate()` returns a single computed value for the entire QuerySet (e.g., total count). `annotate()` adds a computed field to each object in the QuerySet (e.g., employee count per department).

---

## 36. Complete Architecture Summary

```
                          USER (Browser)
                               |
                               | HTTP Request
                               v
                    project/urls.py (ROOT_URLCONF)
                               |
                               v
                         app/urls.py
                               |
                               v
                             View
                         (views.py)
                          /         \
                         /           \
                   Form            Model
               (forms.py)        (models.py)
                   |                  |
               Validation          Django ORM
               cleaned_data           |
                                   Database
                         \           /
                          \         /
                           Template
                          (HTML + DTL)
                               |
                               | HTTP Response (HTML)
                               v
                          USER (Browser)
                               |
                               v
                        CSS / JS / Images
                         (Static Files)
```

**Tests** verify every layer:
```
tests.py
  |-- Model tests     (ORM, data integrity)
  |-- Form tests      (validation logic)
  |-- View tests      (HTTP responses, templates)
  |-- URL tests       (routing, redirects)
  +-- Integration     (complete request flow)
```

---

## 37. Complete CRUD Implementation Reference

### URL Structure

```python
# students/urls.py
from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.student_list, name="list"),
    path("create/", views.student_create, name="create"),
    path("<int:id>/", views.student_detail, name="detail"),
    path("<int:id>/update/", views.student_update, name="update"),
    path("<int:id>/delete/", views.student_delete, name="delete"),
    path("search/", views.student_search, name="search"),
]
```

### Views

```python
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all().order_by("name")
    return render(request, "students/list.html", {"students": students})


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)  # auto 404 if not found
    return render(request, "students/detail.html", {"student": student})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students:list")
    else:
        form = StudentForm()
    return render(request, "students/form.html", {"form": form, "action": "Create"})


def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students:list")
    else:
        form = StudentForm(instance=student)
    return render(request, "students/form.html", {"form": form, "action": "Update"})


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect("students:list")
    return render(request, "students/confirm_delete.html", {"student": student})


def student_search(request):
    query = request.GET.get("q", "")
    students = Student.objects.filter(name__icontains=query) if query else []
    return render(request, "students/search.html", {"students": students, "query": query})
```

### Reusable Form Template (`students/form.html`)

```html
{% load static %}
{% extends "base.html" %}

{% block title %}{{ action }} Student{% endblock %}

{% block content %}
<h1>{{ action }} Student</h1>

<form method="POST">
    {% csrf_token %}

    {% if form.non_field_errors %}
        <div class="alert alert-danger">
            {{ form.non_field_errors }}
        </div>
    {% endif %}

    {{ form.as_p }}

    <button type="submit" class="btn btn-primary">
        {{ action }}
    </button>
    <a href="{% url 'students:list' %}" class="btn btn-secondary">
        Cancel
    </a>
</form>
{% endblock %}
```

---

## 38. Final Internship Checklist

Use this to track your Django understanding:

### Foundation
- [ ] Can create a Django project and app from scratch
- [ ] Understand MVT and can explain the request-response flow
- [ ] Know all key `manage.py` commands by heart
- [ ] Understand `settings.py` key settings and their purpose

### URLs & Views
- [ ] Can define URL patterns with path parameters and converters
- [ ] Can use `include()` and URL namespaces
- [ ] Can use `reverse()` and `{% url %}` for named URLs
- [ ] Can handle query parameters with `request.GET.get()`
- [ ] Comfortable with both FBV and CBV

### Models & Database
- [ ] Can define models with appropriate field types
- [ ] Know all three relationship types and when to use each
- [ ] Can perform all CRUD operations with ORM
- [ ] Know field lookups (`__gt`, `__icontains`, `__in`, etc.)
- [ ] Understand `select_related()` vs `prefetch_related()`
- [ ] Can use Q objects for OR/AND queries
- [ ] Know when to use `get()` vs `filter().first()`

### Templates & Static Files
- [ ] Can use template inheritance with `{% extends %}` and `{% block %}`
- [ ] Know all common template tags and filters
- [ ] Can load and use static files correctly
- [ ] Understand `{% load static %}` and `{% static %}` tag

### Forms & Validation
- [ ] Know the difference between `forms.Form` and `forms.ModelForm`
- [ ] Can implement the full GET/POST form view pattern
- [ ] Can write `clean_<field>()` and `clean()` validation methods
- [ ] Know how `cleaned_data` works
- [ ] Understand `commit=False` and when to use it
- [ ] Know the PRG (Post/Redirect/Get) pattern
- [ ] Always remember `{% csrf_token %}` in POST forms

### Testing
- [ ] Can write model tests, view tests, and form tests
- [ ] Know common assertions (`assertEqual`, `assertContains`, `assertTemplateUsed`, `assertRedirects`)
- [ ] Understand `setUp()` and test isolation
- [ ] Can test authenticated vs unauthenticated views

### Admin
- [ ] Can register models and customize `list_display`, `search_fields`, `list_filter`

---

*Updated for Jay Patel - Python/Django Internship - Stage 4: Django Basics*
*Covers: URL Routing, Static Files, Testing, ORM, Relationships, Forms & Validations*
*Reference: Django Official Documentation - https://docs.djangoproject.com/*
