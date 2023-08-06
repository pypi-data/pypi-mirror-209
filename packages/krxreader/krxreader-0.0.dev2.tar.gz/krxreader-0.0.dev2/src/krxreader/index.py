from .base import KrxBase


class StockIndex(KrxBase):
    def __init__(self, date, start=None, end=None, sector='01', share='2', money='3'):
        super().__init__(date, start, end)

        # '01': KRX
        # '02': KOSPI
        # '03': KOSDAQ
        # '04': 테마
        self._sector = sector
        # '1': 주
        # '2': 천주
        # '3': 백만주
        self._share = share
        # '1': 원
        # '2': 천원
        # '3': 백만원
        # '4': 십억원
        self._money = money

    def index_price(self):
        """[11001] 지수 > 주가지수 > 전체지수 시세
        :return: list
        """
        bld = 'dbms/MDC/STAT/standard/MDCSTAT00101'

        params = {
            'idxIndMidclssCd': self._sector,
            'trdDd': self._date,
            'share': self._share,
            'money': self._money
        }

        return self.fetch_data(bld, params)

    def index_price_change(self):
        """[11002] 지수 > 주가지수 > 전체지수 등락률
        :return: list
        """
        bld = 'dbms/MDC/STAT/standard/MDCSTAT00201'

        params = {
            'idxIndMidclssCd': self._sector,
            'strtDd': self._start,
            'endDd': self._end,
            'share': self._share,
            'money': self._money
        }

        return self.fetch_data(bld, params)


class BondIndex(KrxBase):
    def __init__(self, date, start=None, end=None):
        super().__init__(date, start, end)

    def index_price(self):
        """[11008] 지수 > 채권지수 > 전체지수 시세
        :return:
        """
        bld = 'dbms/MDC/STAT/standard/MDCSTAT00801'

        params = {
            'trdDd': self._date
        }

        return self.fetch_data(bld, params)

    def price_by_index(self, index_type='1'):
        """[11009] 지수 > 채권지수 > 개별지수 시세 추이
        :return:
        """
        bld = 'dbms/MDC/STAT/standard/MDCSTAT00901'

        params = {
            'indTp': index_type,
            'strtDd': self._start,
            'endDd': self._end
        }

        return self.fetch_data(bld, params)
