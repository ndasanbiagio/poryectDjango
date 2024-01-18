from django.urls import path
from . import views

urlpatterns = [
    #Asi para cuando no tiene dinamismo
    # path("january", views.index),
    # path("february", views.february),
    
    #Con dinamismo
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenge)
]