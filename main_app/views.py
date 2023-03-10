from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Art, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid 
import boto3
from django.conf import settings

AWS_ACCESS_KEY = settings.AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
S3_BUCKET = settings.S3_BUCKET
S3_BASE_URL = settings.S3_BASE_URL

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
    fields = ['title', 'type', 'method', 'author_comment', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)
    

def add_photo(request, art_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, S3_BUCKET, key)
            url = f"{S3_BASE_URL}{S3_BUCKET}/{key}"
            photo = Photo(url=url, art_id=art_id)
            photo.save()
        except Exception as error:
            print('Error uploading photo', error)
            return redirect('detail', art_id=art_id)
    return redirect('detail', art_id=art_id)


class ArtUpdate(UpdateView):
    model = Art
    fields = ['title', 'method', 'author_comment', 'description']

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