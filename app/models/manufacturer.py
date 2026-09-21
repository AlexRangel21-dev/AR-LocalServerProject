from sqlalchemy import Column, Integer, String
from database.database import Base


class Manufacturer(Base):
    __tablename__ = "Manufacturer"

    id_manufacturer = Column("id_manufacturer", Integer, primary_key=True)
    manufacturer = Column(String, unique=True)