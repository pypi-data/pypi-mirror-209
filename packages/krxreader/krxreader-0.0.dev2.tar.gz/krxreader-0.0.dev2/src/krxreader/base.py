import csv
import logging

from .fetch import get_json_data
from .fetch import download_csv


class KrxBase:
    def __init__(self, date=None, start=None, end=None):
        self._date = date
        self._start = start
        self._end = end

        self._locale = 'ko_KR'
        self._csvxls_is_no = 'false'

    def fetch_json(self, bld, params):
        payload = {
            'bld': bld,
            'locale': self._locale
        }
        payload.update(params)
        payload.update({
            'csvxls_isNo': self._csvxls_is_no
        })

        logging.debug(payload)

        data = get_json_data(payload)

        return data

    def fetch_data(self, bld, params):
        payload = {
            'locale': self._locale
        }
        payload.update(params)
        payload.update({
            'csvxls_isNo': self._csvxls_is_no,
            'name': 'fileDown',
            'url': bld
        })

        logging.debug(payload)

        csv_str = download_csv(payload)

        reader = csv.reader(csv_str.splitlines())
        data = list(reader)

        return data
