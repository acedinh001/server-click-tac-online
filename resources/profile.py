from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import ProfileModel, SettingModel, DeviceModel, KeywordModel, DomainModel
from schemas import ProfileSchema

blp = Blueprint("Profiles", __name__, description="Operations in profiles")

@blp.route("/profile/<int:profile_id>")
class Profile(MethodView):
    @blp.response(200, ProfileSchema)
    def get(self, profile_id):
        profile = ProfileModel.query.get_or_404(profile_id)
        return profile
    
    def delete(self, profile_id):
        profile = ProfileModel.query.get_or_404(profile_id)
        db.session.delete(profile)
        db.session.commit()
        return {"message": "Profile deleted."}
    
@blp.route("/profile/reset/<int:profile_id>")
class ProfileReset(MethodView):
    def delete(self, profile_id):
        try:
            keywords = KeywordModel.query.filter_by(profile_id=profile_id).all()
            for keyword in keywords:
                db.session.delete(keyword)
                db.session.commit()
            settings = SettingModel.query.filter_by(profile_id=profile_id).all()
            for setting in settings:
                db.session.delete(setting)
                db.session.commit()
            devices = DeviceModel.query.filter_by(profile_id=profile_id).all()
            for device in devices:
                db.session.delete(device)
                db.session.commit()
            domains = DomainModel.query.filter_by(profile_id=profile_id).all()
            for domain in domains:
                db.session.delete(domain)
                db.session.commit()
            return {"message": "Profile reset successfully"}
        except SQLAlchemyError:
            abort(500, message="An error occurred while deleting the keywords.")
            
@blp.route("/profile")
class ProfileList(MethodView):
    @blp.response(200, ProfileSchema(many=True))
    def get(self):
        return ProfileModel.query.all()
    
    @blp.arguments(ProfileSchema)
    @blp.response(201, ProfileSchema)
    def post(self, profile_data):
        profile = ProfileModel(**profile_data)
        try:
            db.session.add(profile)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A profile with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="A error occurred creating the profile.")
        return profile