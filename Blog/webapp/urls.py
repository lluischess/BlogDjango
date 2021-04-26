from django.urls import path
from Blog.webapp.views import home

urlpatterns = [
    path('', home, name="home"),
]