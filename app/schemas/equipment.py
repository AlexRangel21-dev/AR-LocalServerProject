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

class ManufacturerOut(BaseModel):
    id_manufacturer : int 
    manufacturer: str | None = None

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
    model : str | None = None
    serial_number : str | None = None
    asset_number : str | None = None
    next_calibration : str | None = None
    manufacturer : ManufacturerOut | None = None

    class Config:
        from_attributes = True