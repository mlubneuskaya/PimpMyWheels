import sqlalchemy as sa
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from src.models.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = sa.Column(INTEGER(unsigned=True), autoincrement=True, primary_key=True, nullable=False)
    purchase_id = sa.Column(INTEGER(unsigned=True), sa.ForeignKey("transactions.id"), nullable=True, comment="Id transakcji zakupu")
    sale_id = sa.Column(INTEGER(unsigned=True), sa.ForeignKey("transactions.id"), nullable=True, comment="Id transakcji sprzedaży")
    workshop_id = sa.Column(INTEGER(unsigned=True), sa.ForeignKey("workshops.id"), nullable=False, comment="Id warsztatu")
    brand = sa.Column(sa.String(15), nullable=True, comment="Marka pojazdu")

    purchase = relationship("Transaction", foreign_keys=[purchase_id])
    sale = relationship("Transaction", foreign_keys=[sale_id])
    workshop = relationship("Workshop", foreign_keys=[workshop_id])

    def __init__(self, purchase, workshop, brand=None, sale=None):
        self.purchase = purchase
        self.workshop = workshop
        self.brand = brand
        self.sale = sale
