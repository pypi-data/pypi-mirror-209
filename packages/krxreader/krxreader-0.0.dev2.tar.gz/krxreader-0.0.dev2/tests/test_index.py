from krxreader.index import StockIndex


def test_index_price():
    index = StockIndex('20230519')
    data = index.index_price()

    assert data[1][0] == 'KRX 300'
    assert data[1][1] == '1533.13'


def test_index_price_change():
    index = StockIndex('20230519', start='20230511', end='20230519')
    data = index.index_price_change()

    assert data[1][0] == 'KRX 300'
    assert data[1][2] == '1533.13'
