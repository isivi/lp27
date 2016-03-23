import random

from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    landing_version_a = (random.random() > 0.5)

    template = 'lp27_app/home.html'
    context = {'landing_version_a': landing_version_a}
    return render_to_response(template, context, context_instance=RequestContext(request))