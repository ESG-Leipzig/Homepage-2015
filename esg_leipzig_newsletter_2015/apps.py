from django.apps import AppConfig
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy


class ESGLeipzigNewsletter2015AppConfig(AppConfig):
    name = 'esg_leipzig_newsletter_2015'
    verbose_name = ugettext_lazy('Newsletter der ESG Leipzig ab 2015')

    def ready(self):
        """
        Method is called after app loading. Connects the mail_issue
        receiver to Django's post_save signal so we mail every new
        newsletter issue.
        """
        from .signals import mail_issue

        Issue = self.get_model('Issue')
        post_save.connect(
            mail_issue,
            sender=Issue,
            dispatch_uid='mail_issue')
