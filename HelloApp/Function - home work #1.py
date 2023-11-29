# пусть задан такой список people
# посчитать средний возраст по полу в списке

import pandas as pd

people = [
    {"name": "Alice", "age": 10, "gender": "F"},
    {"name": "Bob", "age": 15, "gender": "M"},
    {"name": "David", "age": 40, "gender": "M"},
    {"name": "Charlie", "age": 35, "gender": "M"},
    {"name": "Eve", "age": 30, "gender": "F"}
]


def average_ages_gender(gender: object = "gender") -> object:
    df = pd.DataFrame(people, columns=['name', 'age', 'gender'])
    df_aver_ages = df[df['gender'] == gender]['age'].mean()

    return df_aver_ages


average_ages_gender('F')
average_ages_gender('M')
