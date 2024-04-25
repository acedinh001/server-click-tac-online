from db import db

class ProfileModel(db.Model):
    __tablename__ = 'profiles'
    __mapper_args__ = {
        "confirm_deleted_rows": False,
    }
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    keywords = db.relationship("KeywordModel", back_populates="profile", cascade="all, delete")
    settings = db.relationship("SettingModel", back_populates="profile", cascade="all, delete", uselist=False)
    devices = db.relationship("DeviceModel", back_populates="profile", cascade="all, delete")