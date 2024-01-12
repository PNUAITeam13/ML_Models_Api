import pickle

import pandas as pd

from sklearn.cluster import KMeans

from .models.CSGO_Round_Winner_Clustering.data_transformer.DataTransformer import DataTransformer


with open("app/api/csgo_round_winner_api/pkl/model.pkl", 'rb') as file:
    model = pickle.load(file)

with open("app/api/csgo_round_winner_api/pkl/kmeans.pkl", 'rb') as file:
    kmeans: KMeans = pickle.load(file)


features = ["ct_score", "t_score", "map", "bomb_planted", "ct_money", "t_money", "ct_health", "t_health", "ct_armor",
            "t_armor", "ct_helmets", "t_helmets", "ct_defuse_kits", "ct_players_alive", "t_players_alive",
            "ct_grenade_hegrenade", "t_grenade_hegrenade", "ct_grenade_flashbang", "t_grenade_flashbang",
            "ct_grenade_smokegrenade", "t_grenade_smokegrenade", "ct_grenade_incendiarygrenade",
            "t_grenade_incendiarygrenade", "ct_weapon_ak47", "t_weapon_ak47", "ct_weapon_awp", "t_weapon_awp",
            "ct_weapon_m4a1s", "ct_weapon_m4a4", "ct_weapon_deagle", "t_weapon_deagle"]


class CSGORoundWinnerDataProcessing:

    @staticmethod
    def transform_data(data: pd.DataFrame) -> pd.DataFrame:
        data = data[features]
        transformer = DataTransformer()
        data = transformer.use_ordinal_encoder(data, ["map", "bomb_planted"]).get_data()

        data_cluster = kmeans.fit_predict(data)
        data["Cluster"] = data_cluster

        return data

    @staticmethod
    def predict(data: pd.DataFrame, is_data_transformed: bool = True) -> pd.DataFrame:
        return pd.DataFrame(model.predict(data if is_data_transformed
                                          else CSGORoundWinnerDataProcessing.transform_data(data)))
