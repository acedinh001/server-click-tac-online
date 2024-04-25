from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import SettingModel
from schemas import SettingSchema

blp = Blueprint("Settings", __name__, description="Operations on settings")

@blp.route("/setting/<int:setting_id>")
class Setting(MethodView):
    @blp.response(200, SettingSchema)
    def get(self, setting_id):
        setting = SettingModel.query.get_or_404(setting_id)
        return setting
    
    def delete(self, setting_id):
        setting = SettingModel.query.get_or_404(setting_id)
        db.session.delete(setting)
        db.session.commit()
        return {"message": "Setting deleted."}

@blp.route("/setting")
class SettingList(MethodView):
    @blp.response(200, SettingSchema(many=True))
    def get(self):
        return SettingModel.query.all()

    @blp.arguments(SettingSchema)
    @blp.response(201, SettingSchema)
    def post(self, setting_data):
        setting = SettingModel(**setting_data)
        try:
            db.session.add(setting)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the setting.")
        return setting