from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
    context = {
        'welcome_text': 'Welcome to Todo List App.',
        }
    return render(request, 'todolist.html', context)

def contact(request):
    context = {
        'contact_text': 'Welcome to Contact Page',
        }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text': 'Welcome to About Page',
        }
    return render(request, 'about.html', context)