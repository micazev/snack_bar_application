# backend/sro/MainApplication.py
from interfaces.api.client_api import ClientAPI
from interfaces.api.product_api import ProductAPI
from interfaces.api.order_api import OrderAPI
from infrastructure.database.database_connection import DatabaseConnection
from domain.client import Client
from domain.product import Product
# from domain.order import Order
from config.app_config import Config

def main():
    # Configuração e inicialização da aplicação
    config = Config()
    database_connection = DatabaseConnection(config.database_url)

    # APIs
    client_api = ClientAPI(database_connection)
    product_api = ProductAPI(database_connection)
    order_api = OrderAPI(database_connection)

    # Exemplo de criação de clientes e produtos para teste
    client_data = {"name": "John Doe", "cpf": "12345678901"}
    product_data = {"name": "Pizza", "category": "Food", "price": 20.0, "description": "Delicious pizza"}

    # Criar cliente
    created_client = client_api.create_client(client_data)
    print(f"Created Client: {created_client}")

    # Criar produto
    created_product = product_api.create_product(product_data)
    print(f"Created Product: {created_product}")

    # Exemplo de uso da API de pedidos (fake checkout)
    selected_products = [{"product_id": created_product['id'], "quantity": 2}]
    fake_checkout_result = order_api.fake_checkout(selected_products)
    print(f"Fake Checkout Result: {fake_checkout_result}")

    # ... Resto do código para configurar e iniciar a aplicação ...

if __name__ == "__main__":
    main()
