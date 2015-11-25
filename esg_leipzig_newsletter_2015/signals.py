from django.conf import settings
from django.core.mail import send_mass_mail

from .models import Subscriber


def mail_issue(sender, instance, created, **kwargs):
    """
    Signal receiver to mail every new newsletter issue.
    """
    if created:
        data = (
            (instance.subject,
             instance.text,
             settings.EMAIL_NEWSLETTER_FROM_MAIL,
             [subscriber.email])
            for subscriber in Subscriber.objects.all())
        send_mass_mail(data)
