from bible.bibleapi.asObj import AsObj
from bible.bibleapi.bibleapi import BibleApi


class Bibles(BibleApi):
    _urls = {
        'audio-bibles': '/audio-bibles',
        'audio-bible': 'audio-bibles/%s',
        'audio-books': '/audio-bibles/%s/books',
        'audio-book': '/audio-bibles/%s/books/%s',
        'audio-chapters': '/audio-bibles/%s/books/%s/chapters',
        'audio-chapter': '/audio-bibles/%s/books/%s/chapters/%s',
    }

    def audio_bibles(self):
        return AsObj(**self._call(self._urls['audio-bibles'], ''))

    def audio_bible(self, audio_id):
        return AsObj(**self._call(self._urls['audio-bible'] % audio_id, ''))

    def audio_books(self):
        return AsObj(**self._call(self._urls['audio-books'], ''))

    def audio_book(self, audio_id):
        return AsObj(**self._call(self._urls['audio-book'] % audio_id, ''))

    def audio_books(self):
        return AsObj(**self._call(self._urls['audio-books'], ''))

    def audio_book(self, audio_id):
        return AsObj(**self._call(self._urls['audio-book'] % audio_id, ''))
