# infrastructure/database.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ClientModel(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String, unique=True)

# Configuração do banco de dados
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

# Configuração da sessão do banco de dados
Session = sessionmaker(bind=engine)
