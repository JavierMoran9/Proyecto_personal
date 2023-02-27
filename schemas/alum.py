from pydantic import BaseModel, Field
from typing import Optional, List


class alum(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=5, max_length=15)
    profesor: str = Field(min_length=5, max_length=50)
    curp: str = Field(min_length=5, max_length=50)

    class Config:
        schema_extra = {
            "example":  {
                "id": 1,
                "nombre": "javier moran",
                "profesor": "luis angel",
                "curp": "morj950526",
            }
        }