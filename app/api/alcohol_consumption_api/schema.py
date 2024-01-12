from marshmallow import fields
from app import mm


class AlcoholConsumptionSchema(mm.Schema):
    age = fields.Int()
    studytime = fields.Int()
    reason = fields.Str()
    failures = fields.Int()
    famsup = fields.Str()
    paid = fields.Str()
    activities = fields.Str()
    higher = fields.Str()
    internet = fields.Str()
    romantic = fields.Str()
    famrel = fields.Int()
    freetime = fields.Int()
    goout = fields.Int()
    Dalc = fields.Int()
    Walc = fields.Int()
    absences = fields.Int()

    @staticmethod
    def get_model_details():
        return [
                {"name": "age", "displayName": "Student's age", "type": "int"},
                {"name": "studytime", "displayName": "Weekly study time", "type": "int"},
                {"name": "reason", "displayName": "Reason to choose this school", "type": "multi_select",
                 "options": ["home", "reputation", "course", "other"]},
                {"name": "failures", "displayName": "Number of past class failures", "type": "bool"},
                {"name": "famsup", "displayName": "Family educational support", "type": "bool"},
                {"name": "paid", "displayName": "Extra paid classes within the course subject", "type": "bool"},
                {"name": "activities", "displayName": "Extra-curricular activities", "type": "bool"},
                {"name": "higher", "displayName": "Wants to take higher education", "type": "bool"},
                {"name": "internet", "displayName": "Internet access at home", "type": "bool"},
                {"name": "famrel", "displayName": "Quality of family relationships", "type": "int"},
                {"name": "freetime", "displayName": "Free time after school", "type": "int"},
                {"name": "goout", "displayName": "Going out with friends", "type": "int"},
                {"name": "Dalc", "displayName": "Workday alcohol consumption", "type": "int"},
                {"name": "Walc", "displayName": "Weekend alcohol consumption", "type": "int"},
                {"name": "absences", "displayName": "Number of school absences", "type": "int"}
            ]



