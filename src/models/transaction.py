import sqlalchemy as sa
import enum
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.dialects.mysql import DECIMAL

from src.models.base import Base


class TransactionMethod(sa.enum.Enum):
    cash = 1
    card = 2


class TransactionTypes(sa.enum.Enum):
    income = 1
    cost = 2


class Transaction(Base):
    __tablename__ = "transactions"
    id = sa.Column('id', INTEGER(unsigned=True), primary_key=True, nullable=False, autoincrement=True)
    transaction_method = sa.Column('transaction_method', sa.Enum(TransactionMethod), nullable=False)
    other_party = sa.orm.mapped_column(sa.ForeignKey("customer.id"), nullable=False)
    date = sa.Column('data', sa.Date, nullable=False)
    transaction_type = sa.Column('transaction_type', sa.Enum(TransactionTypes), nullable=False)
    value = sa.Column('value', DECIMAL(precision=8, scale=2, unsigned=True), nullable=False)

    sender = sa.orm.relationship('Customer')

    def init(self, transaction_method, other_party, date, transaction_type, value):
        self.transaction_method = transaction_method
        self.other_party = other_party
        self.date = date
        self.transaction_type = transaction_type
        self.value = value
