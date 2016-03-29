from django.conf.urls import url

from .views import home, recruiter, algorithm, no_stats, stats

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^recruiter/$', recruiter, name='recruiter'),
    url(r'^algorithm/$', algorithm, name='algorithm'),

    # Stats
    url(r'^nostats/$', no_stats, name='no_stats'),
    url(r'^stats/$', stats, name='stats'),
]
