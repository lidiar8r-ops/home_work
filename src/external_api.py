import json.decoder
import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла,3
load_dotenv()
headers = {"apikey": os.getenv("API_KEY")}

url = "https://api.apilayer.com/exchangerates_data/convert"


def get_currency_exchange(transaction: dict) -> float:
    """
    принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
    конвертации суммы операции в рубли.
    :param transaction: транзакция
    :return: сумма транзакции
    """

    try:
        carrency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")
        if carrency_code == "RUB":
            return float(transaction.get("operationAmount", {}).get("amount", 0))
        else:
            amount_transaction = transaction.get("operationAmount", {}).get("amount", 0)
            if not amount_transaction == 0:
                params_load = {"amount": amount_transaction, "from": carrency_code, "to": "RUB"}
                response = requests.get(url=url, params=params_load, headers=headers)
                # print(response)
                if response.status_code == 200:
                    try:
                        return float(response.json()["result"])
                    except json.decoder.JSONDecodeError as e:
                        raise (e)
                else:
                    print(f" Ошибка статус - код: {str(response.status_code)}")
                    return 0
            else:
                return 0
    except Exception as e:
        raise (e)
