from modeltranslation.translator import translator, TranslationOptions
from .models import Event, FlatPage


class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'headline', 'content',)


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(Event, EventTranslationOptions)
