import random
import string

from django.utils.text import slugify

from webapp.models import Article


def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))
    return res


def generate_slug(text):
    new_slug = slugify(text)
    if Article.objects.filter(slug=new_slug).exists():
        generate_slug(text + generate_random_string(5))
    return new_slug
