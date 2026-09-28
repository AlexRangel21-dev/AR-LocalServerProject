from pydantic import BaseModel

class LoginRequest(BaseModel):
    usuario: str
    contraseña: str | None = None 
    pin: str | None = None         

class RegisterRequest(BaseModel):
    nombre: str
    usuario: str
    password: str
    Rol: str = "Visita"
    pin: str | None = None

class UsuarioOut(BaseModel):
    id_usuario: int
    nombre: str
    usuario: str
    Rol: str
    estatus: str

    class Config:
        from_attributes = True

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    rol: str

class UpdatePinRequest(BaseModel):
    usuario: str
    pin: str