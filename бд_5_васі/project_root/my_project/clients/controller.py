# my_project/clients/controller.py
from .service import ClientsService

class ClientsController:
    def __init__(self):
        self.svc = ClientsService()

    def get_all(self):
        return self.svc.get_all()

    def get_by_id(self, client_id: int):
        return self.svc.get_by_id(client_id)

    def create(self, data: dict):
        return self.svc.create(data)

    def update(self, client_id: int, data: dict):
        return self.svc.update(client_id, data)

    def delete(self, client_id: int):
        return self.svc.delete(client_id)
