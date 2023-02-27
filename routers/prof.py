from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.prof import prof as profmodel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.prof import profservice
from schemas.prof import prof

prof_router = APIRouter()


@prof_router.get('/prof', tags=['prof'], response_model=List[prof], status_code=200, dependencies=[Depends(JWTBearer())])
def get_alums() -> List[prof]:
    db = Session()
    result = profservice(db).get_profs()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@prof_router.get('/profs/{id}', tags=['profs'], response_model=prof)
def get_prof(id: int = Path(ge=1, le=2000)) -> prof:
    db = Session()
    result = profservice(db).get_prof(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))



@prof_router.post('/profs', tags=['profs'], response_model=dict, status_code=201)
def create_alum(prof: prof) -> dict:
    db = Session()
    profservice(db).create_prof(prof)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})


@prof_router.put('/profs/{id}', tags=['profs'], response_model=dict, status_code=200)
def update_prof(id: int, prof: prof)-> dict:
    db = Session()
    result = profservice(db).get_alum(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    profservice(db).update_prof(id, prof)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})


@prof_router.delete('/profs/{id}', tags=['profs'], response_model=dict, status_code=200)
def delete_prof(id: int)-> dict:
    db = Session()
    result = db.query(profmodel).filter(profmodel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})
