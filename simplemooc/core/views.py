"""Views."""
from django.shortcuts import render


def home(request):
    """Home page."""
    return render(request, 'home.html')


def contact(request):
    """Contact page."""
    return render(request, 'contact.html')
