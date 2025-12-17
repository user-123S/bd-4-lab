# my_project/bookings/service.py
from .dao import BookingsDAO

class BookingsService:
    def __init__(self):
        self.dao = BookingsDAO()

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, booking_id: int):
        return self.dao.get_by_id(booking_id)

    def create(self, data: dict):
        return self.dao.create(data)

    def update(self, booking_id: int, data: dict):
        return self.dao.update(booking_id, data)

    def delete(self, booking_id: int):
        return self.dao.delete(booking_id)

    def get_by_client(self, client_id: int):
        return self.dao.get_by_client(client_id)
