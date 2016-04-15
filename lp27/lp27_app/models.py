from django.db import models


class Entry(models.Model):
    email = models.EmailField()

    class Meta(object):
        app_label = 'lp27_app'
        verbose_name = u'[Entry] Wpis'
        verbose_name_plural = u'[Entry] Wpisy'
