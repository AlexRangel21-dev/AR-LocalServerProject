from sqlalchemy import Column, Integer, String
from database.database import Base


class Tipo(Base):
    __tablename__ = "Equipment_type"

    id_type = Column("id_type", Integer, primary_key=True)
    name = Column(String, unique=True)