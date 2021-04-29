from django.db import models
from django.utils.text import slugify
from froala_editor.fields import FroalaField

# Create your models here.
from webapp.include import *


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = FroalaField()
    slug = models.SlugField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='webapp/img')
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)

    def __str__(self):
        return f' {self.title} | {self.create_date}'

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Article, self).save(*args, **kwargs)