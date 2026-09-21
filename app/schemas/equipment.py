from pydantic import BaseModel
from datetime import datetime


class EquipoOut(BaseModel):
    display_name: str
    description: str | None = None
    equipment_category: str | None = None
    equipment_type: str | None = None
    last_calibration: datetime | None = None
    manufacturer: str | None = None
    model: str | None = None
    next_calibration: datetime | None = None
    parent: str | None = None
    serial_number: str | None = None

    class Config:
        from_attributes = True