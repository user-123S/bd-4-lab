# my_project/schedules/route.py
from flask import Blueprint, jsonify
from .controller import SchedulesController

bp = Blueprint("schedules", __name__, url_prefix="/schedules")
ctrl = SchedulesController()


@bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())


# M:M — для конкретного розкладу список гідів
@bp.get("/<int:schedule_id>/guides")
def get_guides(schedule_id):
    return jsonify(ctrl.get_guides_for_schedule(schedule_id))
