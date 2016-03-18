from django.template.response import TemplateResponse


def home(request):
    return TemplateResponse(request, 'lp27_app/home.html')
