from django.contrib import admin
from django.urls import path
from yf_django import views  # This is the "Bridge" to your logic

urlpatterns = [
    path('admin/', admin.site.urls),
]