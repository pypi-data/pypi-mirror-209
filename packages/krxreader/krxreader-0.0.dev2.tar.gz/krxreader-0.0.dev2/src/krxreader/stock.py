from .base import KrxBase


class Stock(KrxBase):
    def __init__(self, date, start=None, end=None, market='ALL', share='1', money='1'):
        super().__init__(date, start, end)

        # 'ALL': 전체
        # 'STK': KOSPI
        # 'KSQ': KOSDAQ
        # 'KNX': KONEX
        self._market = market
        # '1': 주
        # '2': 천주
        # '3': 백만주
        self._share = share
        # '1': 원
        # '2': 천원
        # '3': 백만원
        # '4': 십억원
        self._money = money

    def stock_price(self):
        """[12001] 주식 > 종목시세 > 전종목 시세
        :return: list
        """
        bld = 'dbms/MDC/STAT/standard/MDCSTAT01501'

        params = {
            'mktId': self._market,
            'trdDd': self._date,
            'share': self._share,
            'money': self._money
        }

        return self.fetch_data(bld, params)

    def all_listed_issues(self):
        """[12005] 주식 > 종목정보 > 전종목 기본정보
        :return: list
        """
        bld = 'dbms/MDC/STAT/standard/MDCSTAT01901'

        params = {
            'mktId': self._market,
            'share': self._share
        }

        return self.fetch_data(bld, params)
