import json
from unittest.mock import Mock, patch

import pytest

from src.external_api import get_currency_exchange


def test_usd_to_rub_conversion(transaction_params_load_usd, mock_request):
    """Проверка правильной конвертации USD->RUB"""
    # Настройка моков (фиктивных запросов)
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 100.00}
    mock_request.return_value = mock_response

    expected_result = 100
    actual_result = get_currency_exchange(transaction_params_load_usd)
    assert expected_result == actual_result  # сравнение чисел с плавающей точкой


def test_ruble_amount(transaction_params_load_rub):
    """Проверка правильности обработки рублей (без обращения к API)"""
    expected_result = 100.0
    actual_result = get_currency_exchange(transaction_params_load_rub)
    assert expected_result == actual_result


def test_zero_amount():
    """Проверка реакции на операцию с нулевым значением"""
    transaction = {"operationAmount": {"amount": 0, "currency": {"code": "USD"}}}

    expected_result = 0
    actual_result = get_currency_exchange(transaction)
    assert expected_result == actual_result


@pytest.fixture
def mock_request():
    with patch("requests.get") as mocked_get:
        yield mocked_get


def test_http_error(transaction_params_load_usd, mock_request):
    """Проверка реакции на сетевую ошибку (код статуса отличающийся от 200)"""
    mock_response = Mock()
    mock_response.status_code = 404
    mock_request.return_value = mock_response

    expected_result = 0
    actual_result = get_currency_exchange(transaction_params_load_usd)
    assert expected_result == actual_result


def test_json_decode_error(transaction_params_load_usd, mock_request):
    """Проверка реакции на некорректный JSON от API."""
    # Создание мока ответа
    mock_response = Mock()
    mock_response.status_code = 200  # статус успешный, но JSON неправильный
    mock_response.json.side_effect = json.decoder.JSONDecodeError("", "", 0)  # Исключение при чтении JSON
    mock_request.return_value = mock_response  # возвращаем подставленный ответ

    # Ожидается исключение JSONDecodeError
    with pytest.raises(json.decoder.JSONDecodeError):
        get_currency_exchange(transaction_params_load_usd)
