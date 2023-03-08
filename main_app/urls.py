# import dependencies
from django.urls import path
from . import views

# url patterns
urlpatterns = [
    # home
    path('', views.home, name='home'),
    # about
    path('about/', views.about, name='about'),
    # arts paths
    path('arts/', views.arts_index, name='index'),
    path('arts/<int:art_id>', views.arts_detail, name='detail')
]
