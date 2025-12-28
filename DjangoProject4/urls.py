from django.contrib import admin
from django.urls import path, include

from Website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Website.urls')),
]