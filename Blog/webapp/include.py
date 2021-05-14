import random
import string
import logging, sys

from django.utils.text import slugify

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


# Genera letras y numeros aleatorios
# res = ''.join(random.choices(string.ascii_uppercase +
#                                  string.digits, k=random_of_repeats))

def generate_random_string(random_of_repeats):
    res = ''.join(random.choices(string.digits, k=random_of_repeats))
    # logging.debug(res)
    return res


def generate_slug(title):
    new_slug = slugify(title)
    # logging.debug(new_slug)
    from webapp.models import Article
    # if Article.objects.filter(slug=new_slug).exists():
    #     return generate_slug(title + generate_random_string(2))
    return new_slug


# def has_value(cursor, table, column, value):
#     query = 'SELECT 1 from {} WHERE {} = ? LIMIT 1'.format(table, column)
#     return cursor.execute(query, (value,)).fetchone() is not None
