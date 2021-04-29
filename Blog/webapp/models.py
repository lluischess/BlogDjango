from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = FroalaField()
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='webapp/img')
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
