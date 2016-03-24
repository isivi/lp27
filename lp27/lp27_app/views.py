import random

from django.shortcuts import render_to_response
from django.template import RequestContext

from lp27.utils.cookies import set_cookie
from lp27.utils.str import str_to_bool


def home(request):
    landing_version_a = request.COOKIES.get('landing_version_a', None)

    if landing_version_a is None:
        landing_version_a = (random.random() > 0.5)
    else:
        landing_version_a = str_to_bool(landing_version_a)

    template = 'lp27_app/home.html'
    context = {'landing_version_a': landing_version_a}
    response = render_to_response(template, context, context_instance=RequestContext(request))
    set_cookie(response, 'landing_version_a', landing_version_a)
    return response
