# my_project/bookings/route.py
from flask import Blueprint, jsonify, request
from .controller import BookingsController

bp = Blueprint("bookings", __name__, url_prefix="/bookings")
ctrl = BookingsController()


@bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())


@bp.get("/<int:booking_id>")
def get_by_id(booking_id):
    res = ctrl.get_by_id(booking_id)
    if res:
        return jsonify(res)
    return jsonify({"error": "Not found"}), 404


@bp.post("/")
def create():
    data = request.get_json()
    new_id = ctrl.create(data)
    return jsonify({"created_id": new_id}), 201


@bp.put("/<int:booking_id>")
def update(booking_id):
    data = request.get_json()
    updated = ctrl.update(booking_id, data)
    return jsonify({"updated_rows": updated})


@bp.delete("/<int:booking_id>")
def delete(booking_id):
    deleted = ctrl.delete(booking_id)
    return jsonify({"deleted_rows": deleted})


# M:1 — бронювання конкретного клієнта
@bp.get("/by-client/<int:client_id>")
def get_by_client(client_id):
    return jsonify(ctrl.get_by_client(client_id))
