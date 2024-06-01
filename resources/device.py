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
    
@blp.route("/device/profile/<int:profile_id>")
class DeviceByProfile(MethodView):
    def delete(self, profile_id):
        devices = DeviceModel.query.filter_by(profile_id=profile_id).all()
        if not devices:
            abort(404, message="No devices found for the given profile ID.")
        
        try:
            for device in devices:
                db.session.delete(device)
            db.session.commit()
            return {"message": "Devices deleted."}
        except SQLAlchemyError:
            abort(500, message="An error occurred while deleting the devices.")