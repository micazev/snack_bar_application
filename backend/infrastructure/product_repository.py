# infrastructure/product_repository.py
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from domain.product import Product

class ProductRepository:
    def __init__(self, database_connection):
        self.db = database_connection

    def save_product(self, product):
        # Salva um novo produto no banco de dados
        with self.db.connect() as connection:
            with Session(connection) as session:
                session.add(product)
                session.commit()

    def find_products_by_category(self, category):
        # Busca produtos por categoria no banco de dados
        with self.db.connect() as connection:
            with Session(connection) as session:
                products = session.execute(select(Product).filter_by(category=category)).scalars().all()
                return products

    def find_all_products(self):
        # Busca todos os produtos no banco de dados
        with self.db.connect() as connection:
            with Session(connection) as session:
                products = session.execute(select(Product)).scalars().all()
                return products

    def find_product_by_id(self, product_id):
        # Busca um produto por ID no banco de dados
        with self.db.connect() as connection:
            with Session(connection) as session:
                product = session.execute(select(Product).filter_by(id=product_id)).scalar()
                return product

    def update_product(self, product_id, updated_product_data):
        # Atualiza um produto no banco de dados
        with self.db.connect() as connection:
            with Session(connection) as session:
                product = session.execute(select(Product).filter_by(id=product_id)).scalar()
                if product:
                    for key, value in updated_product_data.items():
                        setattr(product, key, value)
                    session.commit()
                return product
