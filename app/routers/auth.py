from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database.deps import get_db
from models.user import Usuario
from schemas.auth import LoginRequest, RegisterRequest, UsuarioOut, LoginResponse, UpdatePinRequest

from core.security import verify_password
from core.auth import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login", response_model=LoginResponse, status_code=200)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    if not request.contraseña and not request.pin:
        raise HTTPException(status_code=400, detail="Debe proporcionar contraseña o pin")

    user = db.query(Usuario).filter(Usuario.usuario == request.usuario).first()

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales Invalidas")

    credencial_valida = False

    if request.contraseña and verify_password(request.contraseña, user.password):
        credencial_valida = True
 
    elif request.pin and user.pin and verify_password(request.pin, user.pin):
        credencial_valida = True

    if not credencial_valida:
        raise HTTPException(status_code=401, detail="Credenciales Invalidas")

    if user.estatus == "Inactivo":
        raise HTTPException(status_code=403, detail="Usuario desactivado")
    
    token = create_access_token({"sub": user.usuario, "rol": user.Rol})
    
    return {
        "access_token": token, 
        "token_type": "bearer", 
        "rol": user.Rol
    }

@router.post("/register", response_model=UsuarioOut, status_code=201)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    if request.pin:
        if len(request.pin) != 4 or not request.pin.isdigit():
            raise HTTPException(status_code=400, detail="El PIN debe contener exactamente 4 números")

    existe = db.query(Usuario).filter(Usuario.usuario == request.usuario).first()

    if existe:
        raise HTTPException(status_code=409, detail="El nombre de usuario ya existe")

    nuevo_usuario = Usuario(
        nombre=request.nombre,
        usuario=request.usuario,
        password=request.password,
        Rol=request.Rol,
        estatus="Activo",
        pin=request.pin 
    )

    db.add(nuevo_usuario)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="El nombre de usuario ya existe")

    db.refresh(nuevo_usuario)
    return nuevo_usuario


@router.put("/set-pin", status_code=200)
def set_pin(request: UpdatePinRequest, db: Session = Depends(get_db)):
    if len(request.pin) != 4 or not request.pin.isdigit():
        raise HTTPException(status_code=400, detail="El PIN debe contener exactamente 4 números")

    user = db.query(Usuario).filter(Usuario.usuario == request.usuario).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    user.pin = request.pin
    db.commit()
    
    return {"message": "PIN asignado correctamente"}