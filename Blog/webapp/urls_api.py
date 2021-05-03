from django.urls import path
from webapp.views import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView),
    path('register/', RegisterView),
]