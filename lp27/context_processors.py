from django.conf import settings


def lp27_settings(request):
    DEBUG = settings.DEBUG
    COMPRESS_ENABLED = settings.COMPRESS_ENABLED

    return {'lp27_settings': locals()}
