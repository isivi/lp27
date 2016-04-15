from django.conf.urls import url

from .views import home, lp2_a, lp2_b, typeform, lp1, recruiter, algorithm, no_stats, stats

urlpatterns = [
    # Second version of LP
    url(r'^$', home, name='home'),
    url(r'^a/$', lp2_a, name='lp2_a'),
    url(r'^b/$', lp2_b, name='lp2_b'),
    url(r'^formularz/$', typeform, name='typeform'),

    # First version of LP
    url(r'^lp1/$', lp1, name='lp1'),
    url(r'^recruiter/$', recruiter, name='recruiter'),
    url(r'^algorithm/$', algorithm, name='algorithm'),

    # Stats
    url(r'^nostats/$', no_stats, name='no_stats'),
    url(r'^stats/$', stats, name='stats'),
]
