# my_project/schedules/dao.py
from db import mysql

class SchedulesDAO:
    # M:M — для кожного розкладу всі гіди
    def get_guides_for_schedule(self, schedule_id: int):
        cur = mysql.connection.cursor()
        query = """
            SELECT 
                ts.id AS schedule_id,
                ts.start_date,
                t.title AS tour_title,
                g.id AS guide_id,
                g.first_name,
                g.last_name,
                g.phone,
                g.specialization
            FROM tour_schedules ts
            JOIN schedule_guides sg ON ts.id = sg.schedule_id
            JOIN guides g ON sg.guide_id = g.id
            JOIN tours t ON ts.tour_id = t.id
            WHERE ts.id = %s
        """
        cur.execute(query, (schedule_id,))
        rows = cur.fetchall()
        cur.close()
        return rows

    # додатково — всі розклади (для тесту)
    def get_all_schedules(self):
        cur = mysql.connection.cursor()
        query = """
            SELECT ts.id, ts.start_date, ts.max_capacity, t.title AS tour_title
            FROM tour_schedules ts
            JOIN tours t ON ts.tour_id = t.id
        """
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        return rows
