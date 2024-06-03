import json
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
with open("data\parameters\description.json", "r") as file:
    descriptions = json.load(file)


class UniquePersonalData:
    phone_numbers = set()
    addresses = set()
    name_surname_pairs = set()


def get_name_surname():
    _, name, sex, _ = names.sample(n=1, weights='frequency').iloc[0]
    if sex == "F":
        surname = female_surnames.sample(n=1, weights='frequency').surname.iloc[0]
    else:
        surname = male_surnames.sample(n=1, weights='frequency').surname.iloc[0]
    return name, surname


def get_unique_name_surname():
    name, surname = get_name_surname()
    while f"{unidecode(name)}{unidecode(surname)}" in UniquePersonalData.name_surname_pairs:
        name, surname = get_name_surname()
    UniquePersonalData.name_surname_pairs.add(f"{unidecode(name)}{unidecode(surname)}")
    return name, surname


def get_phone_number():
    phone_number = str(random.randint(100000000, 999999999))
    while phone_number in UniquePersonalData.phone_numbers:
        phone_number = str(random.randint(100000000, 999999999))
    UniquePersonalData.phone_numbers.add(phone_number)
    return phone_number


def get_address():
    address = mimesis.Address(locale=mimesis.Locale.PL).address()
    while address in UniquePersonalData.addresses:
        address = mimesis.Address(locale=mimesis.Locale.PL).address()
    UniquePersonalData.addresses.add(address)
    return address


def get_birth_date(day):
    min_age = 18
    max_age = 80
    avg_age = 30
    scale = 15
    a, b = (min_age - avg_age) / scale, (max_age - avg_age) / scale
    age = scipy.stats.truncnorm.rvs(a=a, b=b, loc=avg_age, scale=scale)
    return day - timedelta(days=age * 365)


def get_stations_number():
    return int(random.randint(3, 5))


def get_description():
    probabilities = [desc['probability'] for desc in descriptions]

    selected_description = random.choices(descriptions, weights=probabilities, k=1)[0]
    description = selected_description['description']
    parts_cost = selected_description['parts_cost']
    work_cost = selected_description['work_cost']
    return description, parts_cost, work_cost


def get_description_date(day):
    start_date = day + timedelta(days=random.randint(1, 60))

    if random.choice([True, False]):
        return start_date, start_date + timedelta(days=random.randint(1, 30))
    else:
        return start_date, None
