from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def reading(request):
    return HttpResponse("Show the Reading List.")