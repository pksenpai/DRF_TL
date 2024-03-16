from django.urls import path
from .views import *


app_name = 'myapi'
urlpatterns = [
    path('posts/', PostsListAPIView.as_view(), name='Posts'),
    
    # CBV
    path('create/', CreatePostAPIView.as_view(), name='Create'),
    path('read/<int:pk>/', ReadPostAPIView.as_view(), name='Read'),
    path('update/<int:pk>/', UpdatePostAPIView.as_view(), name='Update'),
    path('delete/<int:pk>/', DeletePostAPIView.as_view(), name='Delete'),
    
    # FBV
    path('c/', create_post_view, name='create'),
    path('r/<int:pk>/', read_post_view, name='read'),
    path('u/<int:pk>/', update_post_view, name='update'),
    path('d/<int:pk>/', delete_post_view, name='delete'),
    
    # Unit
    path('uposts/', PostView.as_view(), name='posts'), # use for get & post!
    path('uposts/<int:pk>/', PostView.as_view(), name='post_update'), # use for put, patch & delete!
]
