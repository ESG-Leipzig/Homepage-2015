from django.apps import AppConfig
from django.db.models.signals import pre_delete
from django.utils.translation import ugettext_lazy


class ESGLeipzigHomepage2015AppConfig(AppConfig):
    name = 'esg_leipzig_homepage_2015'
    verbose_name = ugettext_lazy('Homepage der ESG Leipzig ab 2015')

    def ready(self):
        from .signals import mediafile_delete

        MediaFile = self.get_model('MediaFile')
        pre_delete.connect(
            mediafile_delete,
            sender=MediaFile,
            dispatch_uid='mediafile_delete')
