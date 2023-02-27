from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.alum import alum as alummodel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.alum import alumservice
from schemas.alum import alum

alum_router = APIRouter()


@alum_router.get('/alumn', tags=['alumn'], response_model=List[alum], status_code=200, dependencies=[Depends(JWTBearer())])
def get_alums() -> List[alum]:
    db = Session()
    result = alumservice(db).get_alums()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@alum_router.get('/alums/{id}', tags=['alums'], response_model=alum)
def get_alum(id: int = Path(ge=1, le=2000)) -> alum:
    db = Session()
    result = alumservice(db).get_alum(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))



@alum_router.post('/alums', tags=['alums'], response_model=dict, status_code=201)
def create_alum(alum: alum) -> dict:
    db = Session()
    alumservice(db).create_alum(alum)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})


@alum_router.put('/alums/{id}', tags=['alums'], response_model=dict, status_code=200)
def update_alum(id: int, alum: alum)-> dict:
    db = Session()
    result = alumservice(db).get_alum(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    alumservice(db).update_alum(id, alum)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})


@alum_router.delete('/alums/{id}', tags=['alums'], response_model=dict, status_code=200)
def delete_alum(id: int)-> dict:
    db = Session()
    result = db.query(alummodel).filter(alummodel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})
