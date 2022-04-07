import MetaTrader5 as mt
from forex_python.converter import CurrencyRates


def get_pip_value(symbol, account_currency):
    symbol_1 = symbol[0:3]
    symbol_2 = symbol[3:6]
    c = CurrencyRates()
    return c.convert(symbol_2, account_currency, c.convert(symbol_1, symbol_2, 1))