from datetime import datetime, timedelta


def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60

    expires = datetime.now() + timedelta(seconds=max_age)
    response.set_cookie(key, value, max_age=max_age, expires=expires)
