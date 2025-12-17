# my_project/clients/service.py
from .dao import ClientsDAO

class ClientsService:
    def __init__(self):
        self.dao = ClientsDAO()

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, client_id: int):
        return self.dao.get_by_id(client_id)

    def create(self, data: dict):
        return self.dao.create(data)

    def update(self, client_id: int, data: dict):
        return self.dao.update(client_id, data)

    def delete(self, client_id: int):
        return self.dao.delete(client_id)
