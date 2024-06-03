import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.models.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = sa.Column(sa.SmallInteger, autoincrement=True, primary_key=True)
    purchase_id = sa.Column(sa.Integer, sa.ForeignKey("transactions.id"))
    sale_id = sa.Column(sa.Integer, sa.ForeignKey("transactions.id"), nullable=True)

    purchase = relationship("Transaction", foreign_keys=[purchase_id])
    sale = relationship("Transaction", foreign_keys=[sale_id])

    def __init__(self, purchase_id, sale_id=None):
        self.purchase_id = purchase_id
        self.sale_id = sale_id
