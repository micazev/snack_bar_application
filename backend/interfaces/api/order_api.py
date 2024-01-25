# interfaces/api/order_api.py
from application.order.order_service import OrderService

class OrderAPI:
    def __init__(self, database_connection):
        self.order_service = OrderService(database_connection)

    def fake_checkout(self, selected_products):
        order = self.order_service.fake_checkout(selected_products)
        return self._format_order_response(order)

    def _format_order_response(self, order):
        return {
            "order_id": order.order_id,
            "products": order.products,
            "total_price": order.total_price,
        }
