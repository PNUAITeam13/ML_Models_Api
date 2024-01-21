import pandas as pd

from flask import request, make_response
from flask_cors import cross_origin
from marshmallow import ValidationError

from .schema import MobilePricingSchema
from .mobile_pricing_data_processing import MobilePricingDataProcessing

from . import mobile_pricing_bp as app

ALLOWED_EXTENSIONS = {'csv', 'json'}


@app.get('/fields')
@cross_origin()
def get_model_details():
    return MobilePricingSchema.get_model_details()

@app.post('/')
@cross_origin()
def upload_data():
    schema = MobilePricingSchema(many=True)
    data: pd.DataFrame = pd.DataFrame(schema.load(request.json))
    return make_response(MobilePricingDataProcessing.predict(data, is_data_transformed=False).to_json(orient='table'))


@app.post('/upload_file')
@cross_origin()
def upload_file():
    if 'data' not in request.files:
        raise ValidationError('File was not provided')

    data_file = request.files['data']
    filename = data_file.filename

    if '.' in filename and filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
        raise ValidationError('File type not allowed')

    if '.' in filename and filename.rsplit('.', 1)[1].lower() == "csv":
        data = pd.read_csv(data_file)
    else:
        data = pd.read_json(data_file)

    return make_response(MobilePricingDataProcessing.predict(data, is_data_transformed=False).to_json(orient='table'))
