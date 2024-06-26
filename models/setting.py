from db import db

class SettingModel(db.Model):
    __tablename__ = 'settings'
    __mapper_args__ = {
        "confirm_deleted_rows": False,
    }
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80), unique=False, nullable=False)
    is_login_gmail = db.Column(db.Boolean, unique=False, nullable=False)
    time_search_min = db.Column(db.Integer, unique=False, nullable=False)
    time_search_max = db.Column(db.Integer, unique=False, nullable=False)
    time_onpage_min = db.Column(db.Integer, unique=False, nullable=False)
    time_onpage_max = db.Column(db.Integer, unique=False, nullable=False)
    mail_ratio = db.Column(db.Integer, unique=False, nullable=True)
    ads_char = db.Column(db.String(80), unique=False, nullable=False)
    proxy_name = db.Column(db.String(80), unique=False, nullable=False)
    isKeyword1 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword2 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword3 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword4 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword5 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword6 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword7 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword8 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword9 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword10 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword11 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword12 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword13 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword14 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword15 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword16 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword17 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword18 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword19 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword20 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword21 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword22 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword23 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword24 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword25 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword26 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword27 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword28 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword29 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword30 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword31 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword32 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword33 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword34 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword35 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword36 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword37 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword38 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword39 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword40 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword41 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword42 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword43 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword44 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword45 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword46 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword47 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword48 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword49 = db.Column(db.Boolean, unique=False, nullable=False)
    isKeyword50 = db.Column(db.Boolean, unique=False, nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"), unique=False,nullable=False)
    profile = db.relationship("ProfileModel", back_populates="settings")