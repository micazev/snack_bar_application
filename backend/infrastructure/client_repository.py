# infrastructure/client_repository.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from domain.client import Client

Base = declarative_base()

class ClientModel(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String, unique=True)

class ClientRepository:
    def __init__(self, database_connection):
        self.engine = create_engine(database_connection)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_client(self, client):
        with self.Session() as session:
            new_client = ClientModel(name=client.name, cpf=client.cpf)
            session.add(new_client)
            session.commit()

    def find_client_by_id(self, client_id):
        with self.Session() as session:
            client_model = session.query(ClientModel).filter_by(id=client_id).first()
            if client_model:
                return Client(client_model.name, client_model.cpf)
            return None

    def find_client_by_cpf(self, cpf):
        with self.Session() as session:
            client_model = session.query(ClientModel).filter_by(cpf=cpf).first()
            if client_model:
                return Client(client_model.name, client_model.cpf)
            return None
