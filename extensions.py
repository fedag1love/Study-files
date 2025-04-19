import json
import requests
from config import CURRENCIES

class APIException(Exception):
    pass

class CurrenciesConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        try:
            quote_ticker = CURRENCIES[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = CURRENCIES[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/52c48baa29f89e91a3c45690/latest/{quote_ticker}')
        data = json.loads(r.text)

        return data