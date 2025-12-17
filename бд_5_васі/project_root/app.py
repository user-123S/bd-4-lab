# app.py
from flask import Flask, jsonify
import os
from utils.config_loader import load_config
from db import mysql

from my_project.clients.route import bp as clients_bp
from my_project.bookings.route import bp as bookings_bp
from my_project.schedules.route import bp as schedules_bp


def create_app():
    app = Flask(__name__)

    # завантаження конфіга (шлях відносно цього файлу)
    config_path = os.path.join(os.path.dirname(__file__), "config", "app.yml")
    config = load_config(config_path)
    app.config.update(config["mysql"])

    # ініціалізація MySQL
    mysql.init_app(app)

    # реєстрація blueprints
    app.register_blueprint(clients_bp)
    app.register_blueprint(bookings_bp)
    app.register_blueprint(schedules_bp)

    @app.get("/")
    def index():
        return jsonify({"status": "ok", "message": "Tourist agency API is running"})

    @app.get("/health")
    def health():
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT 1")
            cur.fetchone()
            cur.close()
            return jsonify({"status": "ok"}), 200
        except Exception as e:
            return jsonify({
                "details": str(e),
                "message": "Cannot connect to MySQL server",
                "status": "error"
            }), 503

    # обробник помилок підключення до MySQL (повертає дружній JSON)
    try:
        from MySQLdb import OperationalError as MySQLOperationalError

        @app.errorhandler(MySQLOperationalError)
        def handle_mysql_error(error):
            payload = {
                "details": str(error),
                "message": "Cannot connect to MySQL server",
                "status": "error",
            }
            return jsonify(payload), 503
    except Exception:
        # якщо MySQLdb відсутній, мовчимо — інсталяція може використовувати інший драйвер
        pass

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
