from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('myapi.urls')),
    path('accounts/', include('accounts.urls')),
]
