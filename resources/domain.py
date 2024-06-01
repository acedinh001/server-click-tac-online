from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import DomainModel
from schemas import DomainSchema

blp = Blueprint("Domains", __name__, description="Operations on domains")


@blp.route("/domain/<int:domain_id>")
class Domain(MethodView):
    @blp.response(200, DomainSchema)
    def get(self, domain_id):
        domain = DomainModel.query.get_or_404(domain_id)
        return domain

    def delete(self, domain_id):
        domain = DomainModel.query.get_or_404(domain_id)
        db.session.delete(domain)
        db.session.commit()
        return {"message": "Domain deleted."}


@blp.route("/domain")
class DomainList(MethodView):
    @blp.response(200, DomainSchema(many=True))
    def get(self):
        return DomainModel.query.all()

    @blp.arguments(DomainSchema)
    @blp.response(201, DomainSchema)
    def post(self, domain_data):
        domain = DomainModel(**domain_data)
        try:
            db.session.add(domain)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the domain.")
        return domain

@blp.route("/domain/profile/<int:profile_id>")
class DomainByProfile(MethodView):
    def delete(self, profile_id):
        domains = DomainModel.query.filter_by(profile_id=profile_id).all()
        if not domains:
            abort(404, message="No domains found for the given profile ID.")
        
        try:
            for domain in domains:
                db.session.delete(domain)
            db.session.commit()
            return {"message": "Domains deleted."}
        except SQLAlchemyError:
            abort(500, message="An error occurred while deleting the domains.")