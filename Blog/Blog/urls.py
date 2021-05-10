"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from froala_editor import views

from webapp.views import home, login, register, addpost, article_detail

from webapp.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login.html', login, name='login'),
    path('register.html', register, name='register'),
    path('froala_editor/', include('froala_editor.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('webapp.urls_api')),
    path('addpost/', addpost, name='addpost'),
    path('article_detail/<slug>', article_detail, name='article_detail'),
]

# hace que se puedan visualizar los enlaces a las imagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

