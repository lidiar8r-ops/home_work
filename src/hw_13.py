from importlib.metadata import pass_none
import json
import pandas as pd
import re


def avg_age_by_gender(df):
    avg_age_male = df[df["Sex"] == "male"]["Age"].mean()
    avg_age_female = df[df["Sex"] == "female"]["Age"].mean()
    result_dict = {"Мужчины": avg_age_male, "Женщины": avg_age_female}
    return json.dumps(result_dict)


def filter_passengers(df):
    result_df = df[((df["Sex"] == "male") & (df["Age"] > 50)) | ((df["Sex"] == "female") & (df["Age"] < 30))]
    return result_df.to_json(orient="records")


def fare_per_passenger_by_class(df):
    total_fare_by_class = df.groupby("Pclass")["Fare"].sum()
    total_passengers_by_class = df.groupby("Pclass")["PassengerId"].count()
    avg_fare_per_passenger_by_class = total_fare_by_class / total_passengers_by_class
    result_dict = avg_fare_per_passenger_by_class.to_dict()
    return json.dumps(result_dict)


def get_file_scv(filename: str) -> pd.DataFrame:
    result_df = pd.read_csv(filename)
    return result_df


def get_filter_sort_df(df: pd.DataFrame, age_p: int, fare_p: float) -> pd.DataFrame:
    result_df = df.loc[(df["Fare"] < fare_p) & (df["Age"] < age_p)]
    result_df.sort_values("Name")
    # result_df.sort_values("Name", inplace=True)
    return result_df


def get_passenger_class_fare(df: pd.DataFrame) -> json:
    groupby_pass = df.groupby("Pclass").agg({"Fare": "mean", "PassengerId": "count"})

    dict_date = groupby_pass.to_dict(orient="records")
    dict_result = dict()

    # print("-----------------")
    for index, values in enumerate(dict_date):
        dict_result[f"{index+1}st"] = {
            "average_ticket_price": round(values["Fare"], 2),
            "passenger_count": values["PassengerId"],
        }

    return json.dumps(dict_result, indent=4)


def get_passenger_survived(df: pd.DataFrame) -> int:
    passenger_survived = df.loc[(df.Survived == 1)]
    passenger_survived.to_json("..\\data\\passenger_survived.json", orient="records", indent=4, lines=False)
    # with open("..\\data\\passenger_survived1.json", 'w') as f:
    #     json.dump(passenger_survived.to_dict(orient="records"), f, indent=4, ensure_ascii=False)

    return passenger_survived.PassengerId.count()



df_titanic = get_file_scv("..\\data\\titanic.csv")
print(get_file_scv("..\\data\\titanic.csv").head())
print(avg_age_by_gender(df_titanic))
print(get_filter_sort_df(df_titanic, 30, 50.0).head())
print(get_passenger_class_fare(df_titanic))

print(get_passenger_survived(df_titanic))


########################  13_2

# Примеры из лекций
# Компиляция регулярного выражения
pattern = re.compile(r'\d+')

# Поиск всех чисел в строке
text = 'There are 2 apples and 5 bananas'
matches = pattern.finditer(text)

for match in matches:
    print(match)


    