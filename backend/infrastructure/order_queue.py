# infrastructure/order_queue.py
from queue import Queue

class OrderQueue:
    def __init__(self):
        self.queue = Queue()
        self.completed_orders = []

    def enqueue_order(self, order):
        # Adiciona um pedido à fila
        self.queue.put(order)

    def dequeue_order(self):
        # Remove e retorna um pedido da fila
        order = self.queue.get()
        # Adiciona o pedido completo à lista de pedidos completos
        self.completed_orders.append(order)
        return order

    def get_queue_size(self):
        # Retorna o tamanho atual da fila
        return self.queue.qsize()

    def get_all_orders(self):
        # Retorna todos os pedidos completos
        return self.completed_orders

    def clear_queue(self):
        # Limpa a fila e a lista de pedidos completos
        self.queue = Queue()
        self.completed_orders = []
