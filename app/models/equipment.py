from sqlalchemy import Column, String, DateTime
from database.mysql_database import MySQLBase


class Equipo(MySQLBase):
    __tablename__ = "Equipment"

    display_name = Column("Display Name", String(255), primary_key=True)
    description = Column("Description", String(255), nullable=True)
    equipment_category = Column("Equipment category", String(255), nullable=True)
    equipment_type = Column("Equipment Type", String(255), nullable=True)
    last_calibration = Column("Last Calibration", DateTime, nullable=True)
    manufacturer = Column("Manufacturer", String(255), nullable=True)
    model = Column("Model", String(255), nullable=True)
    next_calibration = Column("Next Calibration", DateTime, nullable=True)
    parent = Column("Parent", String(255), nullable=True)
    serial_number = Column("Serial Number", String(255), nullable=True)