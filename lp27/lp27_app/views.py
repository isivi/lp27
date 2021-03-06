import random

from django.conf import settings
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from lp27.lp27_app.forms import EmailForm
from lp27.lp27_app.models import Entry
from lp27.utils.cookies import set_cookie, delete_cookie
from lp27.utils.str import str_to_bool


def home(request):
    version_a = request.COOKIES.get('version_a', None)

    if version_a is None:
        version_a = (random.random() > 0.5)
    else:
        version_a = str_to_bool(version_a)

    if version_a:
        return redirect('lp2_a')
    else:
        return redirect('lp2_b')


def lp2_a(request):
    version_a = request.COOKIES.get('version_a', None)

    if version_a is None:
        version_a = True
    else:
        version_a = str_to_bool(version_a)

    if version_a:
        form = EmailForm()
        template = 'lp27_app/home.html'
        context = {'form': form, 'version_a': True}
        response = render_to_response(template, context, context_instance=RequestContext(request))
        set_cookie(response, 'version_a', version_a)
        return response
    else:
        return redirect('lp2_b')


def lp2_b(request):
    version_a = request.COOKIES.get('version_a', None)

    if version_a is None:
        version_a = False
    else:
        version_a = str_to_bool(version_a)

    if version_a:
        return redirect('lp2_a')
    else:
        form = EmailForm()
        template = 'lp27_app/home.html'
        context = {'form': form, 'version_a': False}
        response = render_to_response(template, context, context_instance=RequestContext(request))
        set_cookie(response, 'version_a', version_a)
        return response


def typeform(request):
    if request.method == 'POST':
        form = EmailForm(data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            Entry.objects.get_or_create(email=email)

    template = 'lp27_app/typeform.html'
    context = {}
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return response


def lp1(request):
    landing_version_a = request.COOKIES.get('landing_version_a', None)

    if landing_version_a is None:
        landing_version_a = (random.random() > 0.5)
    else:
        landing_version_a = str_to_bool(landing_version_a)

    if landing_version_a:
        return redirect('recruiter')
    else:
        return redirect('algorithm')


def recruiter(request):
    landing_version_a = request.COOKIES.get('landing_version_a', None)

    if landing_version_a is None:
        landing_version_a = True
    else:
        landing_version_a = str_to_bool(landing_version_a)

    if landing_version_a:
        template = 'lp27_app/lp1.html'
        context = {'landing_version_a': landing_version_a}
        response = render_to_response(template, context, context_instance=RequestContext(request))
        set_cookie(response, 'landing_version_a', landing_version_a)
        return response
    else:
        return redirect('algorithm')


def algorithm(request):
    landing_version_a = request.COOKIES.get('landing_version_a', None)

    if landing_version_a is None:
        landing_version_a = False
    else:
        landing_version_a = str_to_bool(landing_version_a)

    if landing_version_a:
        return redirect('recruiter')
    else:
        template = 'lp27_app/lp1.html'
        context = {'landing_version_a': landing_version_a}
        response = render_to_response(template, context, context_instance=RequestContext(request))
        set_cookie(response, 'landing_version_a', landing_version_a)
        return response


# Stats

def no_stats(request):
    response = redirect('home')
    set_cookie(response, key=settings.NO_STATS_COOKIE_NAME, value=1)
    return response


def stats(request):
    response = redirect('home')
    delete_cookie(response, key=settings.NO_STATS_COOKIE_NAME)
    return response
