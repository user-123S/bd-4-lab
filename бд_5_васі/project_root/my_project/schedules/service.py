# my_project/schedules/service.py
from .dao import SchedulesDAO

class SchedulesService:
    def __init__(self):
        self.dao = SchedulesDAO()

    def get_all(self):
        return self.dao.get_all_schedules()

    def get_guides_for_schedule(self, schedule_id: int):
        return self.dao.get_guides_for_schedule(schedule_id)
