from django.conf.urls import url

from .views import home, no_stats, stats

urlpatterns = [
    url(r'^$', home),

    # Stats
    url(r'^nostats/$', no_stats, name='no_stats'),
    url(r'^stats/$', stats, name='stats'),
]