from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.



def index(request):
    return HttpResponse("This works!")

def february(request):
    return HttpResponse("Is February")

def monthly_challenges(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Is January"
    elif month == 'february':
        challenge_text = 'Is February'
    elif month == 'march':
        challenge_text = 'Is March'
    elif month == 'april':
        challenge_text = 'Is April'
    else:
       return HttpResponseNotFound("This month is not supported!")      
    return HttpResponse(challenge_text)