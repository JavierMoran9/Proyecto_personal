from models.alum import alum as alummodel
from schemas.alum import alum


class alumservice():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_alum(self):
        result = self.db.query(alummodel).all()
        return result

    def get_alum(self, id):
        result = self.db.query(alummodel).filter(alummodel.id == id).first()
        return result


    def create_alum(self, alum: alum):
        new_alum = alummodel(**alum.dict())
        self.db.add(new_alum)
        self.db.commit()
        return

    def update_alum(self, id: int, data: alum):
        alum = self.db.query(alummodel).filter(alummodel.id == id).first()
        alum.nombre = data.nombre
        alum.profesor = data.profesor
        alum.curp = data.curp
        self.db.commit()
        return