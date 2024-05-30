import random
from datetime import timedelta

import mimesis
import pandas as pd
import scipy
from unidecode import unidecode
import json
from scipy.stats import norm

names = pd.read_csv("data\\parameters\\description.json")
female_surnames = pd.read_csv("data\\female_surnames.csv")
male_surnames = pd.read_csv("data\\male_surnames.csv")
with open("data\\description.json", "r") as file:
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

def get_description():
    n = len(descriptions)
    mean = (n - 1) / 2
    std_dev = n / 6
    probabilities = [norm.pdf(i, mean, std_dev) for i in range(n)]
    total = sum(probabilities)
    probabilities = [p / total for p in probabilities]

    # Randomly select a description based on the generated probabilities using random.choices
    selected_description = random.choices(descriptions, weights=probabilities, k =1)[0]
    description = selected_description['description']
    parts_cost = selected_description['cost_of_parts']
    work_cost = selected_description['cost_of_labor']
    return description, parts_cost, work_cost
