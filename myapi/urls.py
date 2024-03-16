from django.urls import path
from .views import *

# CRUD...
app_name = 'myapi'
urlpatterns = [
    path('posts/', PostView.as_view(), name='posts'), # use for get & post!
    path('posts/<int:pk>/', PostView.as_view(), name='post_update'), # use for put, patch & delete!
    
    #____________________________________________________CRUD_EXAMPLES_________
    # CBV
    path('create/', CreatePostAPIView.as_view(), name='Create'),
    path('read/<str:name>/', ReadPostAPIView.as_view(), name='Read'),
    path('update/<int:pk>/', UpdatePostAPIView.as_view(), name='Update'),
    path('delete/<int:pk>/', DeletePostAPIView.as_view(), name='Delete'),

    # FBV
    path('c/', create_post_view, name='create'),
    path('r/', read_post_view, name='read'),
    path('u/<int:pk>/', update_post_view, name='update'),
    path('d/<int:pk>/', delete_post_view, name='delete'),
]
