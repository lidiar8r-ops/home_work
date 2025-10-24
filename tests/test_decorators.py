import pytest

from src.decorators import log


@log()
def my_function(x, y):
    return x + y


def test_decorator_log(capsys):
    result = my_function(1, 2)
    assert result == 3


def test_log_ok(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


@log()
def my_function_delete(x, y):
    return x / y


def test_log_error():
    with pytest.raises(ValueError):
        my_function_delete(1, 0)


name_file = r"logs\mylog.txt"


@log(filename=name_file)
def my_function_del(x, y):
    return x / y


def test_log_error_file():
    with pytest.raises(ValueError):
        my_function_del(1, 0)


def test_log_ok_file():
    name_file_n = r"logs\mylog.txt"

    @log(filename=name_file_n)
    def my_function_test(x, y):
        return x / y

    my_function_test(1, 2)
    with open(r"logs\mylog.txt", "r", encoding="utf-8") as f:
        text_file = f.read()
    assert "my_function_test ok" in text_file


@log()
def my_function_no_args():
    return "No arguments"


def test_my_function_no_args():
    result = my_function_no_args()
    assert result == "No arguments"


@log()
def my_function_kwargs(x, y, str_kwargs="5"):
    return x + y, str_kwargs


def test_my_function_kwargs(capsys):
    my_function_kwargs(4, 5, 7.2)
    captured = capsys.readouterr()
    assert captured.out[46:-50] == "my_function_kwargs ok"


# Пример простой функции, которую мы украсим нашим декоратором
@log(filename="\\path\\to\\nonexistent\\logfile.log")
def example_function(x: int, y: int) -> int:
    return x + y


# Тест для проверки ошибки FileNotFoundError
def test_decorator_file_not_found_error():
    # Приводим нашу функцию к ошибке путем передачи несуществующего файла
    with pytest.raises(FileNotFoundError):
        example_function(1, 2)
