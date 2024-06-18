import random
from datetime import timedelta

import mimesis
import pandas as pd
import scipy
from scipy.stats import norm
from unidecode import unidecode

names = pd.read_csv("data\\names.csv")
female_surnames = pd.read_csv("data\\female_surnames.csv")
male_surnames = pd.read_csv("data\\male_surnames.csv")


class UniquePersonalData:
    phone_numbers = set()
    addresses = set()
    name_surname_pairs = set()


def get_name_surname():
    _, name, sex, _ = names.sample(n=1, weights="frequency").iloc[0]
    if sex == "F":
        surname = female_surnames.sample(n=1, weights="frequency").surname.iloc[0]
    else:
        surname = male_surnames.sample(n=1, weights="frequency").surname.iloc[0]
    return name, surname


def get_unique_name_surname():
    name, surname = get_name_surname()
    while (
        f"{unidecode(name)}{unidecode(surname)}"
        in UniquePersonalData.name_surname_pairs
    ):
        name, surname = get_name_surname()
    UniquePersonalData.name_surname_pairs.add(f"{unidecode(name)}{unidecode(surname)}")
    return name, surname


def get_phone_number():
    phone_number = str(random.randint(100000000, 999999999))
    while phone_number in UniquePersonalData.phone_numbers:
        phone_number = str(random.randint(100000000, 999999999))
    UniquePersonalData.phone_numbers.add(phone_number)
    return phone_number


def get_address(city):
    address = mimesis.Address(locale=mimesis.Locale.PL).address()
    while address in UniquePersonalData.addresses:
        address = mimesis.Address(locale=mimesis.Locale.PL).address()
    UniquePersonalData.addresses.add(address)
    return f"{address}, {city}"


def get_city():
    return mimesis.Address(locale=mimesis.Locale.PL).city()


def get_birth_date(day):
    min_age = 18
    max_age = 80
    avg_age = 30
    scale = 15
    a, b = (min_age - avg_age) / scale, (max_age - avg_age) / scale
    age = scipy.stats.truncnorm.rvs(a=a, b=b, loc=avg_age, scale=scale)
    return day - timedelta(days=age * 365)


def get_salary(min_salary, avg_salary, max_salary):
    scale = (avg_salary - min_salary) / 2
    a, b = (min_salary - avg_salary) / scale, (max_salary - avg_salary) / scale
    salary = scipy.stats.truncnorm.rvs(a=a, b=b, loc=avg_salary, scale=scale)
    return round(salary, 0)
