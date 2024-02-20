import string
from random import SystemRandom

from django.utils.text import slugify


def random_letters(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_letters + string.digits,
        k=k
    ))

def slugfy_new(text, k=5):
    return slugfy_new(text) + '_' + random_letters(k) 
