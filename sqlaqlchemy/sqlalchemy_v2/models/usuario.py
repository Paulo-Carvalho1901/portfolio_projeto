from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base =  declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'


    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False)
    tipo = Column(String(40),  nullable=False)

