# import dependencies
from django.urls import path
from . import views

# url patterns
urlpatterns = [
    # home
    path('', views.home, name='home'),
    # about
    path('about/', views.about, name='about')
]
