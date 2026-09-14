from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base


class Equipo(Base):
    __tablename__ = "Equipments"

    equipment_name = Column(String, primary_key=True)
    id_category = Column(Integer, ForeignKey("Equipment_Category.id_category"))
    id_type = Column(Integer, ForeignKey("Equipment_type.id_type"))
    status = Column(String, nullable=False, server_default="Active")
    use = Column(Boolean, server_default="False")
    description = Column(String)
    parent_equipment = Column(String, ForeignKey("Equipments.equipment_name"))

    categoria = relationship("Categoria")
    tipo = relationship("Tipo")