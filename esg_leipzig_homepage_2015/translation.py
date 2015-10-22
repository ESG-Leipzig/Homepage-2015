from modeltranslation.translator import TranslationOptions, translator

from .models import Event, FlatPage, News


class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'headline', 'content',)


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(News, NewsTranslationOptions)
