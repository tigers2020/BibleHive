from bible.bibleapi.asObj import AsObj
from bible.bibleapi.bibleapi import BibleApi


class Bible(BibleApi):
    _urls = {
        'bibles': '/bibles',
        'bible': '/bibles/%s',
        'books': '/books',
        'book': '/books/%s',
        'chapters': '/chapters',
        'chapter': '/chapters/%s',
        'verses': '/verses',
        'verse': '/verses/%s',
        'passages': '/passages/%s',
        'bible-sections': '/sections',
        'chapter-sections': '/sections',
        'sections': '/sections/%s',
        'search': '/search',
    }

    def __init__(self):
        super(Bible, self).__init__()
        self.params = {}

    def bible_params(self, language='', abbreviation='', name='', ids=''):
        self.params = {}
        if language != '':
            self.params.update({'language': language})
        if abbreviation != '':
            self.params.update({'abbreviation': abbreviation})
        if name != '':
            self.params.update({'name': name})
        if ids != '':
            self.params.update({'ids': ids})

    def bibles(self, *args, params=None):
        if params is None:
            params = {}

        if args:
            path = self._urls['bible'] % args
        else:
            path = self._urls['bibles']
        return self._get_base_path(path, params)

    def book_params(self, include_chapters=False, include_chapters_and_sections=False):
        self.params = {}
        if include_chapters is not False:
            self.params.update({'include-chapters': include_chapters})
        if include_chapters_and_sections is not False:
            self.params.update({'include-chapters-and-sections': include_chapters_and_sections})

    def books(self, *args, **kwargs):
        querystring = self._get_query_string(kwargs)
        if args:
            return self._get_path(self._urls['book'] % args, querystring)
        else:
            return self._get_path(self._urls['books'], querystring)

    def chapter_params(self, content_type='html', include_notes=False, include_titles=False,
                       include_chapter_numbers=False, include_verse_numbers=False, include_verse_spans=False,
                       parallels=''):
        self.params = {}
        if content_type != 'html':
            self.params.update({'content-type': content_type})
        if include_notes is not False:
            self.params.update({'include-notes': include_notes})
        if include_titles is not False:
            self.params.update({'include-titles': include_titles})
        if include_chapter_numbers is not False:
            self.params.update({'include-chapter-numbers': include_chapter_numbers})
        if include_verse_numbers is not False:
            self.params.update({'include-verse-nulbers': include_verse_numbers})
        if include_verse_spans is not False:
            self.params.update({'include-verse-spans': include_verse_spans})
        if parallels != '':
            self.params.update({'parallels': parallels})

    def chapters(self, *args, **kwargs):
        querystring = self._get_query_string(kwargs)
        if args:
            return self._get_path(self._urls['chapter'] % args, querystring)
        else:
            return self._get_path(self._urls['chapters'], querystring)

    def passage_params(self, content_type='html', include_notes=False, include_titles=False,
                       include_chapter_numbers=False, include_verse_numbers=False, include_verse_spans=False,
                       parallels='', use_org_id=False):
        self.params = {}
        if content_type != 'html':
            self.params.update({'content-type': content_type})
        if include_notes is not False:
            self.params.update({'include-notes': include_notes})
        if include_titles is not False:
            self.params.update({'include-titles': include_titles})
        if include_chapter_numbers is not False:
            self.params.update({'include-chapter-numbers': include_chapter_numbers})
        if include_verse_numbers is not False:
            self.params.update({'include-verse-nulbers': include_verse_numbers})
        if include_verse_spans is not False:
            self.params.update({'include-verse-spans': include_verse_spans})
        if parallels != '':
            self.params.update({'parallels': parallels})
        if use_org_id is not False:
            self.params.update({'use-org-id': use_org_id})

    def passages(self, *args, **kwargs):
        pass

    def section_params(self, content_type='html', include_notes=False, include_titles=False,
                       include_chapter_numbers=False, include_verse_numbers=False, include_verse_spans=False,
                       parallels=''):
        self.params = {}
        if content_type != 'html':
            self.params.update({'content-type': content_type})
        if include_notes is not False:
            self.params.update({'include-notes': include_notes})
        if include_titles is not False:
            self.params.update({'include-titles': include_titles})
        if include_chapter_numbers is not False:
            self.params.update({'include-chapter-numbers': include_chapter_numbers})
        if include_verse_numbers is not False:
            self.params.update({'include-verse-nulbers': include_verse_numbers})
        if include_verse_spans is not False:
            self.params.update({'include-verse-spans': include_verse_spans})
        if parallels != '':
            self.params.update({'parallels': parallels})

    def sections(self, *args, **kwargs):
        pass

    def verse_params(self, content_type='html', include_notes=False, include_titles=False,
                     include_chapter_numbers=False, include_verse_numbers=False, include_verse_spans=False,
                     parallels='', use_org_id=False):
        self.params = {}
        if content_type != 'html':
            self.params.update({'content-type': content_type})
        if include_notes is not False:
            self.params.update({'include-notes': include_notes})
        if include_titles is not False:
            self.params.update({'include-titles': include_titles})
        if include_chapter_numbers is not False:
            self.params.update({'include-chapter-numbers': include_chapter_numbers})
        if include_verse_numbers is not False:
            self.params.update({'include-verse-nulbers': include_verse_numbers})
        if include_verse_spans is not False:
            self.params.update({'include-verse-spans': include_verse_spans})
        if parallels != '':
            self.params.update({'parallels': parallels})
        if use_org_id is not False:
            self.params.update({'use-org-id': use_org_id})

    def verses(self, *args, **kwargs):
        querystring = self._get_query_string(kwargs)
        if args:
            return self._get_path(self._urls['verse'] % args, querystring)
        else:
            return self._get_path(self._urls['verses'], querystring)

    def search_params(self, query='', limit=0, offset=0, sort='relevance', search_range='', fuzziness='AUTO'):
        self.params = {}
        self.params.update({'query': query})
        if limit != 0:
            self.params.update({'limit': limit})
        if offset != 0:
            self.params.update({'offset': offset})
        self.params.update({'sort': sort})
        if search_range != '':
            self.params.update({"search-range": search_range})
        self.params.update({"fuzziness": fuzziness})

    def search(self, query, **kwargs):
        querystring = self._get_query_string(kwargs)
        querystring.update({'query': query})
        return self._get_path(self._urls['search'], querystring)

    @staticmethod
    def _get_query_string(kwargs):
        querystring = {}
        for key in kwargs:
            querystring.update({key: kwargs[key]})
        return querystring

    def response(self):
        return AsObj(**self._call(self.params))
