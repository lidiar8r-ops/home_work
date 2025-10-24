import logging
from typing import Union

logger_masks = logging.getLogger("masks")
file_handler_masks = logging.FileHandler(".\\logs\\masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_masks.setFormatter(file_formatter)
logger_masks.addHandler(file_handler_masks)
logger_masks.setLevel(logging.DEBUG)


def get_mask_card_number(numbers: int) -> Union[str]:
    """Функция маскировки номера банковской карты в виде XXXX XX** **** XXXX, где
    X — это цифра номера.
    :rtype: Union[str]"""
    # проверка на пустую строку
    if not numbers:
        logger_masks.error("Номер карты не может быть пустым")
        raise TypeError("Номер карты не может быть пустым")

    # проверка на тип
    for arg in [numbers]:
        if not isinstance(arg, int):
            logger_masks.error("Ошибка типа данных")
            raise TypeError("Ошибка типа данных")

    str_num = str(numbers)

    # проверка на корректность длины
    if len(str_num) != 16:
        logger_masks.error("Длина номера карты не равна 16")
        raise ValueError("Длина номера карты не равна 16")

    logger_masks.info("Маскировка номера банковской карты прошла успешно")
    return f"{str_num[0:4]} {str_num[4:6]}** **** {str_num[-4:]}"


def get_mask_account(numbers: int) -> Union[str]:
    """Функция маскировки номера банковского счета, Номер счета замаскирован
    и отображается в формате **XXXX, где X — это цифра номера"""
    # проверка на пустую строку
    if not numbers:
        logger_masks.error("Номер счета не может быть пустым")
        raise TypeError("Номер счета не может быть пустым")

    # проверка на тип
    for arg in [numbers]:
        if not isinstance(arg, int):
            logger_masks.error("Ошибка типа данных")
            raise TypeError("Ошибка типа данных")

    str_num = str(numbers)

    # проверка на корректность длины
    if len(str_num) != 20:
        logger_masks.error("Длина номера счета не равна 20")
        raise ValueError("Длина номера счета не равна 20")

    logger_masks.info("Маскировка номера банковского счета прошла успешно")
    return f"**{str_num[-4:]}"
