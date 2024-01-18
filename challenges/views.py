from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


# --------- se iniciaria asi_ ->

# def index(request):
#     return HttpResponse("This works!")

# def february(request):
#     return HttpResponse("Is February")


# --------- Se avanza con el curso, seria otra opcion para cargar.. pero serian 12 una para cada mes

# def monthly_challenge(request, month):
#     # challenge_text = None
#     # if month == 'january':
#     #     challenge_text = "Is January"
#     # elif month == 'february':
#     #     challenge_text = 'Is February'
#     # elif month == 'march':
#     #     challenge_text = 'Is March'
#     # elif month == 'april':
#     #     challenge_text = 'Is April'
#     # else:
#     #    return HttpResponseNotFound("This month is not supported!")      
#     challenge_text = monthly_challenges[month]
#     return HttpResponse(challenge_text)



# Mejorando el dinamismo - con un diccionario
monthly_challenges = {
    "january": "Is January",
    "february": "Is February",
    "march": "Is March",
    "april": "Is April",
    "may": "Is May",
    "june": "Is June",
    "july": "Is July",
    "august": "Is August",
    "september": "Is September",
    "october": "Is October",
    "november": "Is November",
    "december": "Is December"
}

def monthly_challenges_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
