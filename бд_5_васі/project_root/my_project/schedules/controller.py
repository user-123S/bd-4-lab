# my_project/schedules/controller.py
from .service import SchedulesService

class SchedulesController:
    def __init__(self):
        self.svc = SchedulesService()

    def get_all(self):
        return self.svc.get_all()

    def get_guides_for_schedule(self, schedule_id: int):
        return self.svc.get_guides_for_schedule(schedule_id)
