# application/client/client_service.py
from domain.client import Client

# application/client/client_service.py
class ClientService:
    clients = []

    def register_client(self, client_data):
        client_id = len(self.clients) + 1
        new_client = Client(client_id, client_data['name'], client_data['cpf'])
        self.clients.append(new_client)
        return new_client

    def find_client_by_cpf(self, cpf):
        for client in self.clients:
            if client.cpf == cpf:
                return client
        return None