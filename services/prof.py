from models.prof import prof as profmodel
from schemas.prof import prof


class profservice():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_prof(self):
        result = self.db.query(profmodel).all()
        return result

    def get_prof(self, id):
        result = self.db.query(profmodel).filter(profmodel.id == id).first()
        return result

    def create_prof(self, prof: prof):
        new_prof = profmodel(**prof.dict())
        self.db.add(new_prof)
        self.db.commit()
        return

    def update_prof(self, id: int, data: prof):
        prof = self.db.query(profmodel).filter(profmodel.id == id).first()
        prof.nombre = data.nombre
        prof.materia = data.materia
        prof.rfc = data.rfc
        self.db.commit()
        return