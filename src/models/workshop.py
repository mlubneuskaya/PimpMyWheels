import random

import sqlalchemy as sa
from sqlalchemy.dialects.mysql import INTEGER

from src.models.base import Base
from src.generators.personal_data_generator import (
    get_address,
    get_phone_number,
    get_city,
)


class Workshop(Base):
    __tablename__ = "workshops"
    id = sa.Column(
        "id",
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    address = sa.Column("address", sa.String(200), nullable=False)
    phone_number = sa.Column("phone_number", sa.String(12), nullable=False)
    stations_number = sa.Column(
        "number_of_stations", INTEGER(unsigned=True), nullable=False
    )
    opening_date = sa.Column("opening_date", sa.Date, nullable=False)

    def __init__(self, day):
        self.city = get_city()
        self.address = get_address(self.city)
        self.phone_number = get_phone_number()
        self.stations_number = random.randint(3, 5)
        self.opening_date = day
