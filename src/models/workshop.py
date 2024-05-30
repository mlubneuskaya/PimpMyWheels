import sqlalchemy as sa
from src.models.base import Base

from personal_data_generator import get_address, get_phone_number, get_stations_number


class Workshop(Base):
    __tablename__ = "workshops"
    id = sa.Column('id', sa.Integer, primary_key=True)
    address = sa.Column('address', sa.String(255))
    phone_number = sa.Column('phone_number', sa.String(15))
    stations_number = sa.Column('station_number', sa.Integer)
    opening_date = sa.Column('opening_date', sa.Date)

    def __init__(self, day):
        self.address = get_address()
        self.phone_number = get_phone_number()
        self.stations_number = get_stations_number()
        self.opening_date = day