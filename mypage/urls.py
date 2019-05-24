from django.contrib import admin
from django.urls import path
import doyeon.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', doyeon.views.home, name="home"),
]
