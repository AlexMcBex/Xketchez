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
    path('arts/create', views.ArtCreate.as_view(), name='art_create'),
    path('arts/<int:pk>/update/', views.ArtUpdate.as_view(), name='arts_update'),
    path('arts/<int:pk>/delete/', views.ArtDelete.as_view(), name='arts_delete'),
    path('arts/<int:art_id>', views.arts_detail, name='detail'),
]
