import sqlalchemy as sa
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from src.models.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = sa.Column(INTEGER(unsigned=True), autoincrement=True, primary_key=True, nullable=False)
    purchase_id = sa.Column(INTEGER(unsigned=True), sa.ForeignKey("transactions.id", nullable=False))
    sale_id = sa.Column(INTEGER(unsigned=True), sa.ForeignKey("transactions.id"), nullable=True)

    purchase = relationship("Transaction", foreign_keys=[purchase_id])
    sale = relationship("Transaction", foreign_keys=[sale_id])

    def __init__(self, purchase_id, sale_id=None):
        self.purchase_id = purchase_id
        self.sale_id = sale_id
