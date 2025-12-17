# my_project/clients/dao.py
from db import mysql

class ClientsDAO:
    def get_all(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM clients")
        rows = cur.fetchall()
        cur.close()
        return rows

    def get_by_id(self, client_id: int):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM clients WHERE id = %s", (client_id,))
        row = cur.fetchone()
        cur.close()
        return row

    def create(self, data: dict):
        cur = mysql.connection.cursor()
        query = """
            INSERT INTO clients (first_name, last_name, email, phone)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (
            data["first_name"],
            data["last_name"],
            data["email"],
            data["phone"]
        ))
        mysql.connection.commit()
        new_id = cur.lastrowid
        cur.close()
        return new_id

    def update(self, client_id: int, data: dict):
        fields = []
        values = []
        for key in ("first_name", "last_name", "email", "phone"):
            if key in data:
                fields.append(f"{key} = %s")
                values.append(data[key])

        if not fields:
            return 0

        values.append(client_id)
        query = f"UPDATE clients SET {', '.join(fields)} WHERE id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, tuple(values))
        mysql.connection.commit()
        affected = cur.rowcount
        cur.close()
        return affected

    def delete(self, client_id: int):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM clients WHERE id = %s", (client_id,))
        mysql.connection.commit()
        affected = cur.rowcount
        cur.close()
        return affected
