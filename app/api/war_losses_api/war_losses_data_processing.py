import pickle
from datetime import datetime

import pandas as pd
# from models.war_losses.vizual.vizual_lib import VizualLib


with open("app/api/war_losses_api/pkl/model.pkl", 'rb') as file:
    model = pickle.load(file)

# with open("app/api/mobile_pricing_api/pkl/scaler.pkl", 'rb') as file:
#     scaler = pickle.load(file)


features = ['Losses']


class WarLossesDataProcessing:

    @staticmethod
    def transform_data(data: pd.DataFrame) -> pd.DataFrame:
        return data

    @staticmethod
    def predict(date_from, date_to) -> pd.DataFrame:
        reference_date = datetime(2022, 2, 24).date()
        start = (date_from - reference_date).days
        end = (date_to - reference_date).days
        return model.predict(start=start, end=end)
