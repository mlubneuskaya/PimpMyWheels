import sqlalchemy as sa

from src.models.base import Base


class TransactionTypes(sa.enum.Enum):
    cash = 1
    card = 2


class TransactionTypes(sa.enum.Enum):
    cash = 1
    card = 2


class Transaction(Base):
    __tablename__ = "transactions"
    id = sa.Column('id', sa.Integer, primary_key=True)
    transaction_type = sa.Column('transaction type', sa.Enum(TransactionTypes))
    id_sender = sa.orm.mapped_column(sa.ForeignKey("customer.id"))
    date = sa.Column('data', sa.Date)
    topic = sa.Column('topic', sa.Enum())
    value = sa.Column('value', sa.DECIMAL(8, 2))

    sender = sa.orm.relationship('Customer')

    def init(self, id, transaction_type, id_sender, date, topic, value):
        self.id = id
        self.transaction_type = transaction_type
        self.id_sender = id_sender
        self.date = date
        self.topic = topic
        self.value = value
