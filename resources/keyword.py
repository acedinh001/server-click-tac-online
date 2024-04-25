from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import KeywordModel
from schemas import KeywordSchema

blp = Blueprint("Keywords", __name__, description="Operations on keywords")

@blp.route("/keyword/<int:keyword_id>")
class Keyword(MethodView):
    @blp.response(200, KeywordSchema)
    def get(self, keyword_id):
        keyword = KeywordModel.query.get_or_404(keyword_id)
        return keyword
    
    def delete(self, keyword_id):
        keyword = KeywordModel.query.get_or_404(keyword_id)
        db.session.delete(keyword)
        db.session.commit()
        return {"message": "Keyword deleted."}

@blp.route("/keyword")
class KeywordList(MethodView):
    @blp.response(200, KeywordSchema(many=True))
    def get(self):
        return KeywordModel.query.all()

    @blp.arguments(KeywordSchema)
    @blp.response(201, KeywordSchema)
    def post(self, keyword_data):
        keyword = KeywordModel(**keyword_data)
        try:
            db.session.add(keyword)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the keyword.")
        return keyword