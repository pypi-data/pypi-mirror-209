import pytest

from krxreader.fetch import get_json_data
from krxreader.fetch import download_csv


@pytest.fixture
def params():
    """[11001] 지수 > 주가지수 > 전체지수 시세
    :return: dictionary
    """
    return {
        'bld': 'dbms/MDC/STAT/standard/MDCSTAT00101',
        'locale': 'ko_KR',
        'idxIndMidclssCd': '01',
        'trdDd': '20230519',
        'share': '2',
        'money': '3',
        'csvxls_isNo': 'false'
    }


def test_get_json_data(params):
    json = get_json_data(params)
    data = json['output']

    assert data[0]['IDX_NM'] == 'KRX 300'
    assert data[0]['CLSPRC_IDX'] == '1,533.13'


def test_download_csv(params):
    bld = params.pop('bld')
    params['name'] = 'fileDown'
    params['url'] = bld

    csv = download_csv(params)

    lines = csv.splitlines()
    first = lines[1].split(',')

    assert first[0] == '"KRX 300"'
    assert first[1] == '"1533.13"'
