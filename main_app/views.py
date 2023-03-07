from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'home.liquid')

def about(req):
    return render(req, 'about.liquid')