''' 
________________Unauthorized & Forbidden responses________________
if an unauthenticated request is denied permission there are two different error codes:
 - HTTP 401 Unauthorized!
 - HTTP 403 Permission Denied!
'''
from django.urls import path
from .views import *
from rest_framework.authtoken import views as auth_token

app_name = 'accounts'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('auth-token/', auth_token.obtain_auth_token, name='auth_token'),
]

# other ways to create user-token for authenticate
# https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
