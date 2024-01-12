from marshmallow import fields
from app import mm


class MobilePricingSchema(mm.Schema):
    battery_power = fields.Int()
    blue = fields.Str()
    clock_speed = fields.Float()
    dual_sim = fields.Str()
    fc = fields.Int()
    int_memory = fields.Int()
    m_dep = fields.Float()
    mobile_wt = fields.Int()
    n_cores = fields.Int()
    pc = fields.Int()
    px_height = fields.Int()
    px_width = fields.Int()
    ram = fields.Int()
    sc_h = fields.Int()
    sc_w = fields.Int()
    talk_time = fields.Int()
    four_g = fields.Str()
    three_g = fields.Str()
    touch_screen = fields.Str()
    wifi = fields.Str()

    @staticmethod
    def get_model_details():
        return [
            {"name": "battery_power", "displayName": "Battery Power", "type": "int"},
            {"name": "blue", "displayName": "Bluetooth", "type": "str"},
            {"name": "clock_speed", "displayName": "Clock Speed", "type": "float"},
            {"name": "dual_sim", "displayName": "Dual SIM", "type": "str"},
            {"name": "fc", "displayName": "Front Camera", "type": "int"},
            {"name": "int_memory", "displayName": "Internal Memory", "type": "int"},
            {"name": "m_dep", "displayName": "Mobile Depth", "type": "float"},
            {"name": "mobile_wt", "displayName": "Mobile Weight", "type": "int"},
            {"name": "n_cores", "displayName": "Number of Cores", "type": "int"},
            {"name": "pc", "displayName": "Primary Camera", "type": "int"},
            {"name": "px_height", "displayName": "Pixel Height", "type": "int"},
            {"name": "px_width", "displayName": "Pixel Width", "type": "int"},
            {"name": "ram", "displayName": "RAM", "type": "int"},
            {"name": "sc_h", "displayName": "Screen Height", "type": "int"},
            {"name": "sc_w", "displayName": "Screen Width", "type": "int"},
            {"name": "talk_time", "displayName": "Talk Time", "type": "int"},
            {"name": "four_g", "displayName": "4G", "type": "str"},
            {"name": "three_g", "displayName": "3G", "type": "str"},
            {"name": "touch_screen", "displayName": "Touch Screen", "type": "str"},
            {"name": "wifi", "displayName": "WiFi", "type": "str"},
        ]
