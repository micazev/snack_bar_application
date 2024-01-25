# application/product/product_service.py
from domain.product import Product

class ProductService:
    products = []  # armazenamento temporário

    def create_product(self, product_data):
        product_id = len(self.products) + 1
        new_product = Product(
            product_id,
            product_data['name'],
            product_data['category'],
            product_data['price'],
            product_data.get('description', '')
        )
        self.products.append(new_product)
        return new_product

    def edit_product(self, product_data):
        product_id = product_data.get('id')
        if not product_id:
            raise ValueError("ID do produto não fornecido")

        for product in self.products:
            if product.id == product_id:
                product.name = product_data.get('name', product.name)
                product.category = product_data.get('category', product.category)
                product.price = product_data.get('price', product.price)
                product.description = product_data.get('description', product.description)
                return product

        raise ValueError(f"Produto com ID {product_id} não encontrado")

    def remove_product(self, product_id):
        for index, product in enumerate(self.products):
            if product.id == product_id:
                del self.products[index]
                return

        raise ValueError(f"Produto com ID {product_id} não encontrado")

    def find_products_by_category(self, category):
        matching_products = [product for product in self.products if product.category == category]
        return matching_products
