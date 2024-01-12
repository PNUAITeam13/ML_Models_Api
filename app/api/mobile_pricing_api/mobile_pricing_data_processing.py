import pickle

import pandas as pd

from .models.Mobile_Pricing.classifier.logistic_regression import LogisticRegression

with open("app/api/mobile_pricing_api/pkl/model.pkl", 'rb') as file:
    model: LogisticRegression = pickle.load(file)

with open("app/api/mobile_pricing_api/pkl/scaler.pkl", 'rb') as file:
    scaler = pickle.load(file)


features = ['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g', 'int_memory', 'm_dep', 'mobile_wt',
            'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g', 'touch_screen',
            'wifi']


class MobilePricingDataProcessing:

    @staticmethod
    def transform_data(data: pd.DataFrame) -> pd.DataFrame:
        return scaler.transform(data[features])

    @staticmethod
    def predict(data: pd.DataFrame, is_data_transformed: bool = True) -> pd.DataFrame:
        return pd.DataFrame(model.predict(data if is_data_transformed
                                          else MobilePricingDataProcessing.transform_data(data)))
