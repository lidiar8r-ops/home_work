from importlib.metadata import pass_none
from os import path

import pandas as pd
import openpyxl
import csv

import logging
from typing import Union

logger_get_scv_xls = logging.getLogger("get_scv_xls")
file_handler_get_scv_xls = logging.FileHandler(".\\logs\\get_scv_xls.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_get_scv_xls.setFormatter(file_formatter)
logger_get_scv_xls.addHandler(file_handler_get_scv_xls)
logger_get_scv_xls.setLevel(logging.DEBUG)


def get_csv_reader_tansaction(path):
    pass


def get_xls_reader_tansaction(path):
    pass
