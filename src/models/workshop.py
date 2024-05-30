from datetime import date

import sqlalchemy as sa
from src.models.base import Base


class Workshop(Base):
    __tablename__ = "workshops"
    id = sa.Column('id', sa.Integer, primary_key=True)
    address = sa.Column('address', sa.String(255))
    phone_number = sa.Column('phone_number', sa.String(15))
    stations_number = sa.Column('station_number', sa.Integer)
    opening_date = sa.Column('opening_date', sa.Date)
    closing_date = sa.Column('closing_date', sa.Date)  # TODO why?

    def __init__(self):
        self.address = 'address'
        self.phone_number = '111'
        self.stations_number = 0
        self.opening_date = date.today()
        self.closing_date = date.today()
