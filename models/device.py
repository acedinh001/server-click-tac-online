from db import db

class DeviceModel(db.Model):
    __tablename__ = "devices"
    __mapper_args__ = {
        "confirm_deleted_rows": False,
    }
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(80), unique=False, nullable=False)
    appium_port = db.Column(db.Integer, unique=False, nullable=False)
    system_port = db.Column(db.Integer, unique=False, nullable=False)
    key_proxy = db.Column(db.String(80), unique=False, nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"), unique=False,nullable=False)
    profile = db.relationship("ProfileModel", back_populates="devices")
