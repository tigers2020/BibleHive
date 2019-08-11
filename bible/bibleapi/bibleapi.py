# API Wrapper for Digital Bible Platform

import logging
import os
from functools import reduce
from urllib.parse import urljoin, urlunsplit, urlsplit

import requests
from .asObj import AsObj
from .exception import DBpException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DBP_API_KEY = 'DBP_API_KEY'
DBP_LANGUAGE = 'DBP_LANGUAGE'
DBP_VERSION = 'DBP_VERSION'


class BibleApi(object):
    def __init__(self):
        self._base = 'https://api.scripture.api.bible'
        self._version = '/v1'
        self._path = self._base + self._version
        self.url = None

    @property
    def api_key(self):
        return os.environ.get(DBP_API_KEY)

    @api_key.setter
    def api_key(self, api_key):
        os.environ[DBP_API_KEY] = api_key

    @property
    def language(self):
        return os.environ.get(DBP_LANGUAGE)

    @language.setter
    def language(self, language):
        os.environ[DBP_LANGUAGE] = language

    @staticmethod
    def _get_obj(results, key="Title"):
        if 'Title' in results and results['Title'] == "Resource Not Found":
            raise Exception(results['Messages'])
        arr = []
        if key is not None:

            [arr.append(AsObj(**res)) for res in results['key']]
        else:
            return results
        return arr

    def _call(self, params):
        if self.api_key is None or self.api_key == '':
            raise DBpException("No API key Found.")

        headers = {"Content-Type": "application/x-www-form-urlencoded", 'api-key':self.api_key}
        print(self.url)
        print(params)
        req = requests.request('GET', self.url, headers=headers, params=params)
        headers = req.headers
        json = req.json()

        return json

    def _get_base_path(self, path, querystring=None):
        if querystring is None:
            querystring = {}

        self.url = '{base_url}{path}'.format(base_url=self._path, path=path)
        self.param = querystring
        return self

    def _get_path(self, path, querystring=None):
        if querystring is None or querystring == {}:
            querystring = {}

        split_result = list(urlsplit(self._path if self.url is None or self.url == '' else self.url))
        split_result[2] = (str(split_result[2]) + path).replace('//', '/')
        self.url = urlunsplit(split_result)
        self.param = querystring
        return self


