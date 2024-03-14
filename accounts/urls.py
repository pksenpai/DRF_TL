from django.urls import path
from .views import *

# CRUD...
app_name = 'accounts'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    
    # CBV
    # path('read/<str:name>/', ReadPostAPIView.as_view(), name='Read'),
    # path('update/<int:pk>/', UpdatePostAPIView.as_view(), name='Update'),
    # path('delete/<int:pk>/', DeletePostAPIView.as_view(), name='Delete'),

    # # FBV
    # path('c/', create_post_view, name='create'),
    # path('r/', read_post_view, name='read'),
    # path('u/<int:pk>/', update_post_view, name='update'),
    # path('d/<int:pk>/', delete_post_view, name='delete'),
]
