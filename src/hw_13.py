from importlib.metadata import pass_none
from os import path

import pandas as pd
import openpyxl
import csv
import json



def get_file_scv(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)
    return df

import pandas as pd


def avg_age_by_gender(df):
    avg_age_male = df[df['Sex'] == 'male']['Age'].mean()
    avg_age_female = df[df['Sex'] == 'female']['Age'].mean()
    result_dict = {'Мужчины': avg_age_male, 'Женщины': avg_age_female}
    return json.dumps(result_dict)


def filter_passengers(df):
    result_df = df[((df['Sex'] == 'male') & (df['Age'] > 50)) | ((df['Sex'] == 'female') & (df['Age'] < 30))]
    return result_df.to_json(orient='records')

def fare_per_passenger_by_class(df):
    total_fare_by_class = df.groupby('Pclass')['Fare'].sum()
    total_passengers_by_class = df.groupby('Pclass')['PassengerId'].count()
    avg_fare_per_passenger_by_class = total_fare_by_class / total_passengers_by_class
    result_dict = avg_fare_per_passenger_by_class.to_dict()
    return json.dumps(result_dict)


df_titanic = get_file_scv('..\\data\\titanic.csv')
print(get_file_scv('..\\data\\titanic.csv').head())
print(avg_age_by_gender(df_titanic))

