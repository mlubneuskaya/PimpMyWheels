import sqlalchemy as sa

class TransactionTypes(sa.enum.Enum):
    cash = 1
    card = 2
class Transaction:
    __tablename__ = "transactions"
    id = sa.Column('id', sa.Integer, primary_key=True)
    transaction_type = sa.Column('transaction type', sa.Enum(TransactionTypes))
    id_sender = sa.Column('sender id', sa.Integer)
    id_recipient = sa.Column('recipient id', sa.Integer)
    date = sa.Column('data', sa.Date)
    topic = sa.Column('topic', sa.String(25))
    value = sa.Column('value', sa.DECIMAL(8, 2))
    
    
    def init(self, id, transaction_type, id_sender, id_recipient, date, topic, value):
        self.id = id
        self.transaction_type = transaction_type
        self.id_sender = id_sender
        self.id_recipient = id_recipient
        self.date = date
        self.topic = topic
        self.value = value