from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.deps import get_mysql_db
from models.equipment import Equipo
from schemas.equipment import EquipoOut

router = APIRouter(
    prefix="/equipments",
    tags=["Equipments"]
)


@router.get("/{parent}/children", response_model=List[EquipoOut])
def get_children(parent: str, db: Session = Depends(get_mysql_db)):
    padre = db.query(Equipo).filter(Equipo.display_name == parent).first()

    if not padre:
        raise HTTPException(
            status_code=404,
            detail=f"El equipo '{parent}' no existe"
        )

    hijos = db.query(Equipo).filter(
        Equipo.parent == parent
    ).all()

    return hijos