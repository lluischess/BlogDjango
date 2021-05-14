from django.contrib import admin

# Register your models here.
from webapp.models import Article, Profile

admin.site.register(Article)
admin.site.register(Profile)
