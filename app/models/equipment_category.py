from sqlalchemy import Column, Integer, String
from database.database import Base


class Categoria(Base):
    __tablename__ = "Equipment_Category"

    id_category = Column("id_category", Integer, primary_key=True)
    name = Column(String, unique=True)