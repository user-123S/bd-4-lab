# my_project/bookings/dao.py
from db import mysql

class BookingsDAO:
    def get_all(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bookings")
        rows = cur.fetchall()
        cur.close()
        return rows

    def get_by_id(self, booking_id: int):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bookings WHERE id = %s", (booking_id,))
        row = cur.fetchone()
        cur.close()
        return row

    def create(self, data: dict):
        cur = mysql.connection.cursor()
        query = """
            INSERT INTO bookings (client_id, schedule_id, status_id, total_price)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (
            data["client_id"],
            data["schedule_id"],
            data["status_id"],
            data["total_price"]
        ))
        mysql.connection.commit()
        new_id = cur.lastrowid
        cur.close()
        return new_id

    def update(self, booking_id: int, data: dict):
        fields = []
        values = []
        for key in ("client_id", "schedule_id", "status_id", "total_price"):
            if key in data:
                fields.append(f"{key} = %s")
                values.append(data[key])
        if not fields:
            return 0

        values.append(booking_id)
        query = f"UPDATE bookings SET {', '.join(fields)} WHERE id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, tuple(values))
        mysql.connection.commit()
        affected = cur.rowcount
        cur.close()
        return affected

    def delete(self, booking_id: int):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM bookings WHERE id = %s", (booking_id,))
        mysql.connection.commit()
        affected = cur.rowcount
        cur.close()
        return affected

    # M:1 — для конкретного клієнта всі його бронювання
    def get_by_client(self, client_id: int):
        cur = mysql.connection.cursor()
        query = """
            SELECT 
                b.id AS booking_id,
                b.total_price,
                b.booking_date,
                bs.status_name,
                ts.id AS schedule_id,
                ts.start_date,
                t.title AS tour_title
            FROM bookings b
            JOIN booking_statuses bs ON b.status_id = bs.id
            JOIN tour_schedules ts ON b.schedule_id = ts.id
            JOIN tours t ON ts.tour_id = t.id
            WHERE b.client_id = %s
        """
        cur.execute(query, (client_id,))
        rows = cur.fetchall()
        cur.close()
        return rows
