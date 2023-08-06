from krxreader.stock import Stock

from .utils import save_csv


def stock_price(date, filename):
    stock = Stock(date)
    output = stock.stock_price()

    assert output[0][4] == '종가'
    assert output[1][4] != ''

    save_csv(output, filename)
