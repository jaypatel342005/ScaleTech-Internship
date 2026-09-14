from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

data = [{
        "name": "Jay",
        "age": 21,
        "role": "AI/ML Developer",
        "isStudent": True,
        "courses": ["Python", "Machine Learning", "Deep Learning"],
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "zipcode": "10001"
        },
        "grades": None
    },
    {
        "name": "John",
        "age": 30,
        "role": "Software Engineer",
        "isStudent": True,
        "courses": ["Python", "Machine Learning", "Deep Learning"],
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "zipcode": "10001"
        },
        "grades": None
    }
    ]


def members(request):
    return JsonResponse(data , safe=False)
