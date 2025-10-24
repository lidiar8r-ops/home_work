from importlib.metadata import pass_none
import json
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame


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


def get_file_scv(filename: str) -> pd.DataFrame:
    result_df = pd.read_csv(filename)
    return result_df

def get_filter_sort_df(df: DataFrame, age_p: int, fare_p: float) -> pd.DataFrame:
    result_df = df[(df.Fare < fare_p) & (df.Age < age_p)]
    result_df.sort_values('Name', inplace=True)
    return result_df


def get_passenger_class_fare(df: DataFrame) -> json:
    new_pclass = df.groupby('Pclass')
    new_fare = df.groupby('Pclass')['Fare'].mean()
    new_passenger_count = df.groupby('Pclass')['PassengerId'].count()
    result_dict = {f"{new_pclass}st": {"average_ticket_price": new_fare, "passenger_count": new_passenger_count}}
    return result_dict


df_titanic = get_file_scv('..\\data\\titanic.csv')
print(get_file_scv('..\\data\\titanic.csv').head())
print(avg_age_by_gender(df_titanic))
print(get_filter_sort_df(df_titanic, 30, 50.0).head())
print(get_passenger_class_fare(df_titanic))

