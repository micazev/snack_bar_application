# domain/product.py
class Product:
    def __init__(self, product_id, name, category, price, description):
        self.id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.description = description


