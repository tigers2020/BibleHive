from django.conf import settings
from django.db import models

from .bibleapi import bibleapi
from .bibleapi.libraries.bible import Bible


# Create your models here.


class BibleApiMixin:
    def __init__(self):
        self.BibleApi = bibleapi.BibleApi
        self.BibleApi.api_key = settings.BIBLE_API_KEY
        self.Bible = Bible


class Language(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=126, default='')
    nameLocal = models.CharField(max_length=126, default='')
    script = models.CharField(max_length=32, default='')
    scriptDirection = models.CharField(max_length=6, default='LTR')


class Country(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=256, default='')
    nameLocal = models.CharField(max_length=256, default='')


class AudioBible(models.Model):
    pass


class BibleManager(models.Manager, BibleApiMixin):
    def check_data(self, bibleId):
        try:
            obj = Bible.objects.get(id=bibleId)
        except Bible.DoesNotExist:
            obj = None

        return obj

    def get_data(self, bibleId):
        obj = self.check_data(bibleId)
        if obj:
            return obj
        data = self.Bible.bibles(bibleId).response()
        obj_data = {}
        for key in data.entries:
            if key == 'copyright':
                cr_obj = CopyRight.ApiObjects.get_data(bibleId)

            obj_data[key] = data.entries.get(key)

        obj = self.create(obj_data)
        return obj


class Bible(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    dblId = models.CharField(max_length=16, unique=True)
    relatedDbl = models.CharField(max_length=32, null=True, blank=True)
    name = models.CharField(max_length=256, default='')
    nameLocal = models.CharField(max_length=256, default='')
    abbreviation = models.CharField(max_length=16, default='')
    abbreviationLocal = models.CharField(max_length=16, default='')
    description = models.TextField(null=True, blank=True)
    descriptionLocal = models.TextField(null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    countries = models.ManyToManyField(Country, related_name='countries+')
    type = models.CharField(max_length=8, default='text')
    updatedAt = models.DateTimeField(null=True, blank=True)
    audioBibles = models.ForeignKey(AudioBible, on_delete=models.CASCADE)
    Objects = models.Manager()
    ApiObjects = BibleManager()


class CopyRightManager(models.Manager, BibleApiMixin):
    def check_data(self, bibleId):
        try:
            obj = CopyRight.objects.get(bibleId__id=bibleId)
        except CopyRight.DoesNotExist:
            obj = None
        return obj

    def create_data(self, bibleId):
        data = self.Bible.bibles(bibleId).response()

        data_obj = {'bibleId': Bible.ApiObjects.get_data(bibleId)}

        for key in data.entries:
            if key == 'copyright':
                data_obj[key] = data.entries.get(key)
        obj = self.create(**data_obj)
        return obj

    def get_data(self, bibleId):
        obj = self.check_data(bibleId)
        if obj:
            return obj
        else:
            obj = self.create_data(bibleId)

        return obj


class CopyRight(models.Model):
    bibleId = models.ForeignKey(Bible, on_delete=models.CASCADE)
    copyright = models.TextField(null=True, blank=True)
    ApiObjects = CopyRightManager()


class Book(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    bibleId = models.ForeignKey(Bible, on_delete=models.CASCADE, null=True, blank=True)
    abbreviation = models.CharField(max_length=3, default='')
    name = models.CharField(max_length=16, default='')
    nameLong = models.CharField(max_length=64, default='')


class Chapter(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    bibleId = models.ForeignKey(Bible, on_delete=models.CASCADE, null=True, blank=True)
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    reference = models.CharField(max_length=16, default='')
    number = models.CharField(max_length=8, default='0')
    position = models.IntegerField(default=0)
    content = models.TextField(default='')
    next = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='Chapter.next+')
    previous = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='Chapter.previous+')


class Verse(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    orgId = models.CharField(max_length=8, unique=True, default='')
    bibleId = models.ForeignKey(Bible, on_delete=models.CASCADE, null=True, blank=True)
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    chapterId = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)
    reference = models.CharField(max_length=16, default='')
