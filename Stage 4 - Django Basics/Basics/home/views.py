from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

data = [
    {
    "name": "jay",
    "age": 21,
    "role": "AI/ML Developer",
    },
    {
    "name": "john",
    "age": 22,
    "role": "Full Stack Developer",
    },
    {
    "name" : "rohan",
    "age": 23,
    "role": "Software Engineer",
    },
    {
    "name" : "sachin",
    "age": 34,
    "role": "Devops Engineer",
    },
    {
    "name" : "raj",
    "age": 25,
    "role": "Data Scientist",
    }
]


def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "about/about.html" , context = {"data" : data})