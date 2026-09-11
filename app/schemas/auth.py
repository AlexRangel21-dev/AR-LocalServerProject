from pydantic import BaseModel


class LoginRequest(BaseModel):
    usuario: str
    password: str


class RegisterRequest(BaseModel):
    nombre: str
    usuario: str
    password: str
    id_rol: int | None = None


class UsuarioOut(BaseModel):
    id_usuario: int
    nombre: str
    usuario: str
    id_rol: int | None = None

    class Config:
        from_attributes = True