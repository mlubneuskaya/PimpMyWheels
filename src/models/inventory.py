import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER

from src.models.base import Base


class Inventory(Base):
    __tablename__ = "inventory"
    id = sa.Column(
        INTEGER(unsigned=True),
        autoincrement=True,
        primary_key=True,
        comment="Id inwentarza",
    )
    equipment_id = sa.Column(
        INTEGER(unsigned=True),
        sa.ForeignKey("equipment.id"),
        nullable=False,
        comment="Id wyposażenia",
    )
    service_id = sa.Column(
        INTEGER(unsigned=True),
        sa.ForeignKey("services.id"),
        nullable=True,
        comment="Id usługi",
    )
    workshop_id = sa.Column(
        INTEGER(unsigned=True),
        sa.ForeignKey("workshops.id"),
        nullable=False,
        comment="Id warsztatu",
    )
    delivery_date = sa.Column("delivery_date", sa.Date, nullable=False)

    equipment = relationship("Equipment", back_populates="inventories")  # TODO
    service = relationship("Service")
    workshop = relationship("Workshop")

    def __init__(self, delivery_date, equipment, workshop, part_name):
        self.equipment = equipment
        self.service = None
        self.workshop = workshop
        self.delivery_date = delivery_date
        self.part = part_name
