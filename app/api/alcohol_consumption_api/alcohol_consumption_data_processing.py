import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

with open("app/api/alcohol_consumption_api/pkl/model.pkl", 'rb') as file:
    model: RandomForestClassifier = pickle.load(file)

with open("app/api/alcohol_consumption_api/pkl/encoder.pkl", 'rb') as file:
    encoder = pickle.load(file)

with open("app/api/alcohol_consumption_api/pkl/OH_encoder.pkl", 'rb') as file:
    oh_encoder = pickle.load(file)

bool_cols = ['famsup', 'paid', 'activities', 'higher', 'internet', 'romantic']
OH_cols = ['reason']
alcohol_features = ['age', 'studytime', 'reason', 'failures', 'famsup', 'paid', 'activities', 'higher', 'internet',
                    'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'absences']


class AlcoholConsumptionDataProcessing:

    @staticmethod
    def transform_data(data: pd.DataFrame) -> pd.DataFrame:
        data = data[alcohol_features]
        data[bool_cols] = encoder.transform(data[bool_cols])
        oh_data = pd.DataFrame(oh_encoder.transform(data[OH_cols]))
        oh_data.index = data.index
        num_data = data.drop(OH_cols, axis=1)
        oh_data = pd.concat([num_data, oh_data], axis=1)
        oh_data.columns = oh_data.columns.astype(str)
        return oh_data

    @staticmethod
    def predict(data: pd.DataFrame, is_data_transformed: bool = True) -> pd.DataFrame:
        return pd.DataFrame(model.predict(data if is_data_transformed
                                          else AlcoholConsumptionDataProcessing.transform_data(data)))
