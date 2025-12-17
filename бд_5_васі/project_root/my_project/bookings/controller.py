# my_project/bookings/controller.py
from .service import BookingsService

class BookingsController:
    def __init__(self):
        self.svc = BookingsService()

    def get_all(self):
        return self.svc.get_all()

    def get_by_id(self, booking_id: int):
        return self.svc.get_by_id(booking_id)

    def create(self, data: dict):
        return self.svc.create(data)

    def update(self, booking_id: int, data: dict):
        return self.svc.update(booking_id, data)

    def delete(self, booking_id: int):
        return self.svc.delete(booking_id)

    def get_by_client(self, client_id: int):
        return self.svc.get_by_client(client_id)
