from datetime import datetime

from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to the meeting planner")


def date(request):
    return HttpResponse("This page was served at: " + str(datetime.now()))
