from db import db

class DomainModel(db.Model):
    __tablename__ = "domains"
    __mapper_args__ = {
        "confirm_deleted_rows": False,
    }
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(200), unique=False, nullable=False)
    profile_id = db.Column(
        db.Integer, db.ForeignKey("profiles.id"), unique=False, nullable=False
    )
    profile = db.relationship("ProfileModel", back_populates="domains")
