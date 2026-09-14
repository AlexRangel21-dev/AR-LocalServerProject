from pydantic import BaseModel


class CategoriaOut(BaseModel):
    id_category: int
    name: str | None = None

    class Config:
        from_attributes = True


class TipoOut(BaseModel):
    id_type: int
    name: str | None = None

    class Config:
        from_attributes = True


class EquipoOut(BaseModel):
    equipment_name: str
    categoria: CategoriaOut | None = None
    tipo: TipoOut | None = None
    status: str
    use: bool
    description: str | None = None
    parent_equipment: str | None = None

    class Config:
        from_attributes = True