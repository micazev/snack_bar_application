# domain/order.py
class Order:
    def __init__(self, order_id, products, total_price):
        self.order_id = order_id
        self.products = products
        self.total_price = total_price

    def __repr__(self):
        return f"Order(order_id={self.order_id}, products={self.products}, total_price={self.total_price})"
