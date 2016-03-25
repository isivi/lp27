from __future__ import absolute_import

from django.conf import settings


def stats_off(request):
    return settings.NO_STATS_COOKIE_NAME in request.COOKIES


def stats_on(request):
    return settings.NO_STATS_COOKIE_NAME not in request.COOKIES
