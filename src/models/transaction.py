import sqlalchemy as sa

from src.models.base import Base


class TransactionMethod(sa.enum.Enum):
    cash = 1
    card = 2


class TransactionTypes(sa.enum.Enum):
    income = 1
    cost = 2


class Transaction(Base):
    __tablename__ = "transactions"
    id = sa.Column('id', sa.Integer, primary_key=True)
    transaction_method = sa.Column('transaction_method', sa.Enum(TransactionMethod))
    other_party = sa.orm.mapped_column(sa.ForeignKey("customer.id"))
    date = sa.Column('data', sa.Date)
    transaction_type = sa.Column('transaction_type', sa.Enum(TransactionTypes))
    value = sa.Column('value', sa.DECIMAL(8, 2))

    sender = sa.orm.relationship('Customer')

    def init(self, id, transaction_method, other_party, date, transaction_type, value):
        self.id = id
        self.transaction_method = transaction_method
        self.other_party = other_party
        self.date = date
        self.transaction_type = transaction_type
        self.value = value
