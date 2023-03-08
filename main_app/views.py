from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Art
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def arts_index(req):
    arts= Art.objects.all()
    return render(req, 'arts/index.html', { 'arts' : arts })

def arts_detail(req, art_id):
    art= Art.objects.get(id=art_id)
    return render(req, 'arts/detail.html', { 'art': art })

class ArtCreate(CreateView):
    model = Art
    fields = '__all__'

class ArtUpdate(UpdateView):
    model = Art
    fields = ['title', 'method', 'comment', 'description']

class ArtDelete(DeleteView):
    model = Art
    success_url = '/arts/'


def signup(request):
# this view is going to be like our class based views
# because this is going to be able to handle a GET and a POST request
    error_message = ''
    if request.method == 'POST':
        # this is how to create a user form object that includes data from the browser
        form = UserCreationForm(request.POST)
        # now we check validity of the form, and handle our success and error situations
        if form.is_valid():
            # we'll add the user to the database
            user = form.save()
            # then we'll log the user in
            login(request, user)
            # redirect to our index page
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # a bad POST or GET request will render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)