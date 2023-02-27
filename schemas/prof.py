from pydantic import BaseModel, Field
from typing import Optional, List


class prof(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=5, max_length=30)
    materia: str = Field(min_length=5, max_length=50)
    rfc: str = Field(min_length=5, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "nombre": "luis angel",
                "materia": "matematicas",
                "rfc": "morj950526",
            }
        }