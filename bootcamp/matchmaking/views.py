from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
# Create your views here.

def matches(request):
    matches = page_user = User.objects.all()
    return render(request, 'matchmaking/carousel.html', {'matches': matches})
    #return render(request, 'matchmaking/carousel.html')
