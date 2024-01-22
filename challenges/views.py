from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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



# Mejorando el dinamismo - con un diccionario - sin if/elif
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
    "december": None
}


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h2>Invalid month</h2>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenges/january - ex.
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    # try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>" - Old form
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        
        # Not use -> return HttpResponse(response_data)
    # except:
        return HttpResponseNotFound("<h2>This month is not supported!</h2>")
    

#New view - Menu of the month

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })
    
    
    
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    # responde_data =  f"<ul>{list_items}</ul>"
    # return HttpResponse(responde_data)