from django.urls import path, include

from Blog.webapp import views

urlpatterns = [
    path('', views.home, name="home"),
]