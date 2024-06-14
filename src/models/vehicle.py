import sqlalchemy as sa
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from src.models.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = sa.Column(INTEGER(unsigned=True), autoincrement=True, primary_key=True, nullable=False)
    purchase_id = sa.Column(INTEGER(unsigned=True), sa.ForeignKey("transactions.id"), nullable=False, comment="Id transakcji zakupu")
    sale_id = sa.Column(INTEGER(unsigned=True), sa.ForeignKey("transactions.id"), nullable=True, comment="Id transakcji sprzedaży")
    workshop_id = sa.Column(INTEGER(unsigned=True), sa.ForeignKey("workshops.id"), nullable=False, comment="Id warsztatu")
    brand = sa.Column(sa.String(15), nullable=True, comment="Marka pojazdu")

    purchase = relationship("Transaction", foreign_keys=[purchase_id])
    sale = relationship("Transaction", foreign_keys=[sale_id])
    workshop = relationship("Workshop")

    def __init__(self, purchase_id, workshop_id, brand=None, sale_id=None):
        self.purchase_id = purchase_id
        self.workshop_id = workshop_id
        self.brand = brand
        self.sale_id = sale_id
