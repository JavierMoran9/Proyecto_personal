from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class prof(Base):

    __tablename__ = "profesor"

    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    materia = Column(String)
    rfc = Column(String)
    