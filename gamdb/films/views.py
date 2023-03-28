from django.shortcuts import render
from .models import Movie

def homepage(request):
    context = {
        "movie": Movie.objects.all(),
    }
    return render (request, 'main.html', context)

