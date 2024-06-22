import sqlalchemy as sa
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from src.models.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = sa.Column(
        INTEGER(unsigned=True), autoincrement=True, primary_key=True, nullable=False
    )
    purchase_id = sa.orm.mapped_column(sa.ForeignKey("transactions.id"), nullable=True)
    sale_id = sa.orm.mapped_column(sa.ForeignKey("transactions.id"), nullable=True)
    workshop_id = sa.orm.mapped_column(sa.ForeignKey("workshops.id"), nullable=False)
    brand = sa.Column(sa.String(15), nullable=True, comment="Marka pojazdu")
    model = sa.Column(sa.String(15), nullable=True, comment="Model pojazdu")

    purchase = relationship("Transaction", foreign_keys=[purchase_id])
    sale = relationship("Transaction", foreign_keys=[sale_id])
    workshop = relationship("Workshop", foreign_keys=[workshop_id])

    def __init__(self, purchase, workshop, brand=None, model=None, sale=None):
        self.purchase = purchase
        self.workshop = workshop
        self.brand = brand
        self.model = model
        self.sale = sale
