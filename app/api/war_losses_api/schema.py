from marshmallow import fields
from app import mm


class WarLossesSchema(mm.Schema):
    date_from = fields.Date()
    date_to = fields.Date()

    @staticmethod
    def get_model_details():
        return [
            {"name": "date_from", "displayName": "Date from", "type": "date"},
            {"name": "date_to", "displayName": "Date to", "type": "date"},
        ]
