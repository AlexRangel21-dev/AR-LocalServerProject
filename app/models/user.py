from sqlalchemy import Column, Integer, String, ForeignKey, event
from database.database import Base
from core.security import hash_password


class Usuario(Base):
    __tablename__ = "Users"

    id_usuario = Column(Integer, primary_key=True)
    id_rol = Column(Integer, ForeignKey("Roles.id_rol"))

    nombre = Column(String, nullable=False)
    usuario = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


def _es_hash_bcrypt(valor: str) -> bool:
    return valor.startswith(("$2a$", "$2b$", "$2y$"))


@event.listens_for(Usuario, "before_insert")
@event.listens_for(Usuario, "before_update")
def _hashear_password_automaticamente(mapper, connection, target: Usuario):
    if target.password and not _es_hash_bcrypt(target.password):
        target.password = hash_password(target.password)