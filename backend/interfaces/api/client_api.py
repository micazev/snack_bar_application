# interfaces/api/client_api.py
from application.client.client_service import ClientService

class ClientAPI:
    def __init__(self):
        self.client_service = ClientService()

    def create_client(self, client_data):
        new_client = self.client_service.register_client(client_data)
        return {
            "message": "Cliente criado com sucesso!",
            "client": {
                "id": new_client.id,
                "name": new_client.name,
                "cpf": new_client.cpf,
            }
        }

    def get_client_by_cpf(self, cpf):
        found_client = self.client_service.find_client_by_cpf(cpf)

        if found_client:
            return {
                "message": "Cliente encontrado!",
                "client": {
                    "id": found_client.id,
                    "name": found_client.name,
                    "cpf": found_client.cpf,
                }
            }
        else:
            return {
                "message": "Cliente não encontrado.",
                "client": None
            }