from django.conf import settings

from lp27.utils.nostats import stats_on


def lp27_settings(request):
    DEBUG = settings.DEBUG
    COMPRESS_ENABLED = settings.COMPRESS_ENABLED
    FUNCTIONS = settings.FUNCTIONS

    is_stats_request = stats_on(request)

    return {'lp27_settings': locals()}
