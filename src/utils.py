import json
from typing import Any


def get_list_transaction(path_file: str) -> list[Any]:
    """
    принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    :return:
    :param path_file: путь до JSON-файла
    """
    data = list()
    try:
        with open(path_file, encoding="utf-8") as f:
            data = json.load(f)
        return list(data)
    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
