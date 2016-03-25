from datetime import timedelta
from django.utils import timezone


def set_cookie(response, key, value, days_expire=None):
    if days_expire is None:
        max_age = 365  # one year
    else:
        max_age = days_expire

    expires = timezone.now() + timedelta(days=max_age)
    response.set_cookie(key=key, value=value, max_age=max_age, expires=expires)


def delete_cookie(response, key):
    response.delete_cookie(key=key)
