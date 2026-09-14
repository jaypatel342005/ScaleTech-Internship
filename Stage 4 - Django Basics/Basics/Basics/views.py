from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse



def home(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("about page")