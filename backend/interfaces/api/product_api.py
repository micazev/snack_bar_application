# interfaces/api/product_api.py
from application.product.product_service import ProductService

class ProductAPI:
    def __init__(self, database_connection):
        self.product_service = ProductService(database_connection)

    def create_product(self, product_data):
        product = self.product_service.create_product(product_data)
        return self._format_product_response(product)
    
    def edit_product(self, product_data):
        edited_product = self.product_service.edit_product(product_data)
        return self._format_product_response(edited_product)

    def remove_product(self, product_id):
        self.product_service.remove_product(product_id)
        return {"message": "Produto removido com sucesso!"}

    def get_products_by_category(self, category):
        products = self.product_service.find_products_by_category(category)
        return [self._format_product_response(product) for product in products]

    def fake_checkout(self, selected_products):
        return {"message": "Fake checkout realizado com sucesso!", "selected_products": selected_products}

    def _format_product_response(self, product):
        return {
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "price": product.price,
            "description": product.description,
        }
