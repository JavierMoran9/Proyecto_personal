from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class alum(Base):

    __tablename__ = "alum"

    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    profesor = Column(String)
    curp = Column(String)
    