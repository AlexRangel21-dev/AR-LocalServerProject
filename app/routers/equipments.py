from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from database.deps import get_mysql_db
from models.equipment import Equipo
from schemas.equipment import EquipoOut
from core.auth import get_current_user

router = APIRouter(
    prefix="/equipments",
    tags=["Equipments"]
)


@router.get("/{parent}/children", response_model=List[EquipoOut])
def get_children(
    parent: str,
    db: Session = Depends(get_mysql_db),
    current_user: dict = Depends(get_current_user)
):
    parent_clean = parent.strip()

    padre = db.query(Equipo).filter(
        func.trim(Equipo.parent) == parent_clean
    ).first()

    if not padre:
        raise HTTPException(
            status_code=404,
            detail=f"El equipo '{parent}' no existe"
        )

    hijos = db.query(Equipo).filter(
        func.trim(Equipo.parent) == parent_clean
    ).all()

    return hijos