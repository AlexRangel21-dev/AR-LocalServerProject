from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database.deps import get_db
from models.user import Usuario
from schemas.auth import LoginRequest, RegisterRequest, UsuarioOut
from core.security import verify_password
from core.auth import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.query(Usuario).filter(
        Usuario.usuario == request.usuario
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales Invalidas")

    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciales Invalidas")

    token = create_access_token({
        "sub": user.usuario,
        "rol": user.id_rol
    })

    return {"access_token": token, "token_type": "bearer"}


@router.post("/register", response_model=UsuarioOut, status_code=201)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    existe = db.query(Usuario).filter(
        Usuario.usuario == request.usuario
    ).first()

    if existe:
        raise HTTPException(status_code=409, detail="El nombre de usuario ya existe")

    nuevo_usuario = Usuario(
        nombre=request.nombre,
        usuario=request.usuario,
        password=request.password,
        id_rol=request.id_rol
    )

    db.add(nuevo_usuario)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="El nombre de usuario ya existe")

    db.refresh(nuevo_usuario)
    return nuevo_usuario