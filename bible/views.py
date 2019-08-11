from django.conf import settings
# Create your views here.
from django.views.generic import TemplateView

from .bibleapi.bibleapi import BibleApi
from .bibleapi.libraries.bible import Bible


class BaseMixin:
    def __init__(self):
        self.bibleApi = BibleApi
        self.bibleApi.api_key = settings.BIBLE_API_KEY
        self.bible = Bible()


class BibleIndexView(BaseMixin, TemplateView):
    template_name = 'bible/index.html'

    def get_context_data(self, **kwargs):
        context = super(BibleIndexView, self).get_context_data(**kwargs)
        bible = self.bible.bibles('de4e12af7f28f599-01').chapters('gen.8')

        context['bibles'] = bible.response()
        return context


class BibleView(BaseMixin, TemplateView):
    template_name = 'bible/bibles.html'

    def get_context_data(self, **kwargs):
        context = super(BibleView, self).get_context_data(**kwargs)
        bibleId = kwargs['bibleId']
        bible = self.bible.bibles(bibleId)

        context['bibles'] = bible.response()


class BooksView(BaseMixin, TemplateView):
    template_name = 'bible/books.html'

    def __init__(self, *args, **kwargs):
        super(BooksView, self).__init__(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(BooksView, self).get_context_data(**kwargs)
        bibleId = kwargs['bibleId']
        print('bible_id', bibleId)
        bibles = self.bible.bibles(bibleId)
        books = bibles.books()
        books.book_params(include_chapters=True)
        context['bibles'] = bibles.response()
        context['books'] = books.response()
        return context
