from datetime import date

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.models.generator import get_name, get_phone_number, get_surname, get_address, get_birth_date

Base = declarative_base()
def get_base():
    return Base
