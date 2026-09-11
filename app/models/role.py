from sqlalchemy import Column, Integer, String
from database.database import Base


class Rol(Base):
    __tablename__ = "Roles"

    id_rol = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)