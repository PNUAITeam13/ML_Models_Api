import pandas as pd
import calplot

from flask import request, send_file
from flask_cors import cross_origin
from matplotlib import pyplot as plt

from .schema import WarLossesSchema
from .war_losses_data_processing import WarLossesDataProcessing

import io

from . import war_losses_bp as app

ALLOWED_EXTENSIONS = {'csv', 'json'}


@app.get('/fields')
@cross_origin()
def get_model_details():
    return WarLossesSchema.get_model_details()


@app.get("/calendar")
@cross_origin()
def get_calendar():
    return send_file(path_or_file="./api/war_losses_api/images/data_analysis_calendar.png", mimetype='image/png')


@app.get("/graphic")
@cross_origin()
def get_graphic():
    return send_file(path_or_file="./api/war_losses_api/images/data_analysis_graphic.png", mimetype='image/png')


@app.post('/predict/calendar')
@cross_origin()
def predict_calendar():
    schema = WarLossesSchema()
    data: WarLossesSchema = schema.load(request.json)
    data_predict = WarLossesDataProcessing.predict(data["date_from"], data["date_to"])
    values = pd.Series(data_predict, index=data_predict.index)

    calplot.calplot(values,
                    cmap='RdBu',
                    figsize=(20, 13),
                    suptitle='Calendar',
                    suptitle_kws={'x': 0.5, 'y': 1.0})

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')


@app.post('/predict/graphic')
@cross_origin()
def predict_graphic():
    schema = WarLossesSchema()
    data: WarLossesSchema = schema.load(request.json)
    data_predict = WarLossesDataProcessing.predict(data["date_from"], data["date_to"])
    _, _ = plt.subplots(nrows=1, ncols=1, figsize=(15, 5))

    plt.subplot(1, 1, 1)
    plt.plot(data_predict, label='Expected Values')
    plt.legend(loc="upper left")
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')
