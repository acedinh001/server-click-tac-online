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
