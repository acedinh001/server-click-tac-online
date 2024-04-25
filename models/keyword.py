from db import db 

class KeywordModel(db.Model):
    __tablename__ = 'keywords'
    __mapper_args__ = {
        "confirm_deleted_rows": False,
    }
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(80), unique=False, nullable=False)
    combo = db.Column(db.Integer, unique=False, nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"), unique=False,nullable=False)
    profile = db.relationship("ProfileModel", back_populates="keywords")