from marshmallow import Schema, fields


class PlainProfileSchema(Schema):
    id = fields.Int(dump_only=True, autoincrement=True)
    name = fields.Str()
    
class PlainKeywordSchema(Schema):
    id = fields.Int(dump_only=True, autoincrement=True)
    value = fields.Str()
    combo = fields.Int()
    
class PlainSettingSchema(Schema):
    id = fields.Int(dump_only=True, autoincrement=True)
    location = fields.Str()
    is_login_gmail = fields.Bool()
    time_search_min = fields.Int()
    time_search_max = fields.Int()
    time_onpage_min = fields.Int()
    time_onpage_max = fields.Int()
    exclude_domains = fields.Str()
    ads_char = fields.Str()
    proxy_name = fields.Str()
    isKeyword1 = fields.Bool()
    isKeyword2 = fields.Bool()
    isKeyword3 = fields.Bool()
    isKeyword4 = fields.Bool()
    isKeyword5 = fields.Bool()
    isKeyword6 = fields.Bool()
    isKeyword7 = fields.Bool()
    isKeyword8 = fields.Bool()
    isKeyword9 = fields.Bool()
    isKeyword10 = fields.Bool()
    isKeyword11 = fields.Bool()
    isKeyword12 = fields.Bool()
    isKeyword13 = fields.Bool()
    isKeyword14 = fields.Bool()
    isKeyword15 = fields.Bool()
    isKeyword16 = fields.Bool()
    isKeyword17 = fields.Bool()
    isKeyword18 = fields.Bool()
    isKeyword19 = fields.Bool()
    isKeyword20 = fields.Bool()
    isKeyword21 = fields.Bool()
    isKeyword22 = fields.Bool()
    isKeyword23 = fields.Bool()
    isKeyword24 = fields.Bool()
    isKeyword25 = fields.Bool()
    isKeyword26 = fields.Bool()
    isKeyword27 = fields.Bool()
    isKeyword28 = fields.Bool()
    isKeyword29 = fields.Bool()
    isKeyword30 = fields.Bool()
    isKeyword31 = fields.Bool()
    isKeyword32 = fields.Bool()
    isKeyword33 = fields.Bool()
    isKeyword34 = fields.Bool()
    isKeyword35 = fields.Bool()
    isKeyword36 = fields.Bool()
    isKeyword37 = fields.Bool()
    isKeyword38 = fields.Bool()
    isKeyword39 = fields.Bool()
    isKeyword40 = fields.Bool()
    isKeyword41 = fields.Bool()
    isKeyword42 = fields.Bool()
    isKeyword43 = fields.Bool()
    isKeyword44 = fields.Bool()
    isKeyword45 = fields.Bool()
    isKeyword46 = fields.Bool()
    isKeyword47 = fields.Bool()
    isKeyword48 = fields.Bool()
    isKeyword49 = fields.Bool()
    isKeyword50 = fields.Bool()
    
class PlainDeviceSchema(Schema):
    id = fields.Int(dump_only=True, autoincrement=True)
    device_name = fields.Str()
    appium_port = fields.Int()
    system_port = fields.Int()
    key_proxy = fields.Str()

class ProfileSchema(PlainProfileSchema):
    settings = fields.Nested(PlainSettingSchema(), dump_only=True)
    devices = fields.List(fields.Nested(PlainDeviceSchema()), dump_only=True)
    keywords = fields.List(fields.Nested(PlainKeywordSchema()), dump_only=True)
    
class SettingSchema(PlainSettingSchema):
    profile_id = fields.Int(required=True, load_only=True)
    profile = fields.Nested(PlainProfileSchema(), dump_only=True)
    
class DeviceSchema(PlainDeviceSchema):
    profile_id = fields.Int(required=True, load_only=True)
    profile = fields.Nested(PlainProfileSchema(), dump_only=True)
    
class KeywordSchema(PlainKeywordSchema):
    profile_id = fields.Int(required=True, load_only=True)
    profile = fields.Nested(PlainProfileSchema(), dump_only=True)
    
    