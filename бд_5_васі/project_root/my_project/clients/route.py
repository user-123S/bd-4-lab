# my_project/clients/route.py
from flask import Blueprint, jsonify, request
from .controller import ClientsController

bp = Blueprint("clients", __name__, url_prefix="/clients")
ctrl = ClientsController()


@bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())


@bp.get("/<int:client_id>")
def get_by_id(client_id):
    res = ctrl.get_by_id(client_id)
    if res:
        return jsonify(res)
    return jsonify({"error": "Not found"}), 404


@bp.post("/")
def create():
    data = request.get_json()
    new_id = ctrl.create(data)
    return jsonify({"created_id": new_id}), 201


@bp.put("/<int:client_id>")
def update(client_id):
    data = request.get_json()
    updated = ctrl.update(client_id, data)
    return jsonify({"updated_rows": updated})


@bp.delete("/<int:client_id>")
def delete(client_id):
    deleted = ctrl.delete(client_id)
    return jsonify({"deleted_rows": deleted})
