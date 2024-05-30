import random
from datetime import timedelta

import mimesis
import pandas as pd
import scipy

names = pd.read_csv("data\\names.csv")
female_surnames = pd.read_csv("data\\female_surnames.csv")
male_surnames = pd.read_csv("data\\male_surnames.csv")


def get_name():
    _, name, gender, _ = names.sample(n=1, weights='frequency').iloc[0]
    return name, gender


def get_surname(gender):
    if gender == "F":
        return female_surnames.sample(n=1, weights='frequency').surname.iloc[0]
    else:
        return male_surnames.sample(n=1, weights='frequency').surname.iloc[0]


def get_phone_number():
    return str(random.randint(100000000, 999999999))


def get_address():
    return mimesis.Address(locale=mimesis.Locale.PL).address()


def get_birth_date(day):
    min_age = 18
    max_age = 80
    avg_age = 30
    scale = 15
    a, b = (min_age - avg_age) / scale, (max_age - avg_age) / scale
    age = scipy.stats.truncnorm.rvs(a=a, b=b, loc=avg_age, scale=scale)
    return day - timedelta(days=age * 365)
