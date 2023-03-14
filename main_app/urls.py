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
    path('arts/mine', views.arts_mine, name='arts_mine'),
    path('arts/create', views.ArtCreate.as_view(), name='art_create'),
    path('arts/user/<int:user_id>', views.arts_user, name='arts_user'),
    path('arts/<int:pk>/update/', views.ArtUpdate.as_view(), name='arts_update'),
    path('arts/<int:pk>/delete/', views.ArtDelete.as_view(), name='arts_delete'),
    path('arts/<int:art_id>/add_photo', views.add_photo , name='add_photo'),
    path('arts/<int:art_id>/add_comment/', views.add_comment, name='add_comment'),
    path('arts/<int:art_id>', views.arts_detail, name='detail'),
    # path('arts/<int:art_id>/comments/<int:pk>/delete', views.CommentDelete.as_view(), name='comment_delete'),
    path('accounts/signup/', views.signup, name='signup')
]
