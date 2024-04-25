from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import DeviceModel
from schemas import DeviceSchema

blp = Blueprint("Devices", __name__, description="Operations on devices")

@blp.route("/device/<int:device_id>")
class Device(MethodView):
    @blp.response(200, DeviceSchema)
    def get(self, device_id):
        device = DeviceModel.query.get_or_404(device_id)
        return device
    
    def delete(self, device_id):
        device = DeviceModel.query.get_or_404(device_id)
        db.session.delete(device)
        db.session.commit()
        return {"message": "Device deleted."}

@blp.route("/device")
class DeviceList(MethodView):
    @blp.response(200, DeviceSchema(many=True))
    def get(self):
        return DeviceModel.query.all()

    @blp.arguments(DeviceSchema)
    @blp.response(201, DeviceSchema)
    def post(self, device_data):
        device = DeviceModel(**device_data)
        try:
            db.session.add(device)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the device.")
        return device