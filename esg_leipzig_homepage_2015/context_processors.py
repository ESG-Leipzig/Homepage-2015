from .models import FlatPage


def flatpages(request):
    """
    Adds a queryset of all flatpages to the template context.
    """
    return {'flatpages': FlatPage.objects.all()}
