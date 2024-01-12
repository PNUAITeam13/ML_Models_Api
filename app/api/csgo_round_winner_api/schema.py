from marshmallow import fields
from app import mm


class CSGORoundWinnerSchema(mm.Schema):
    ct_score = fields.Int()
    t_score = fields.Int()
    map = fields.Str()
    bomb_planted = fields.Bool()
    ct_money = fields.Int()
    t_money = fields.Int()
    ct_health = fields.Int()
    t_health = fields.Int()
    ct_armor = fields.Int()
    t_armor = fields.Int()
    ct_helmets = fields.Int()
    t_helmets = fields.Int()
    ct_defuse_kits = fields.Int()
    ct_players_alive = fields.Int()
    t_players_alive = fields.Int()
    ct_grenade_hegrenade = fields.Int()
    t_grenade_hegrenade = fields.Int()
    ct_grenade_flashbang = fields.Int()
    t_grenade_flashbang = fields.Int()
    ct_grenade_smokegrenade = fields.Int()
    t_grenade_smokegrenade = fields.Int()
    ct_grenade_incendiarygrenade = fields.Int()
    t_grenade_incendiarygrenade = fields.Int()
    ct_weapon_ak47 = fields.Int()
    t_weapon_ak47 = fields.Int()
    ct_weapon_awp = fields.Int()
    t_weapon_awp = fields.Int()
    ct_weapon_m4a1s = fields.Int()
    ct_weapon_m4a4 = fields.Int()
    ct_weapon_deagle = fields.Int()
    t_weapon_deagle = fields.Int()

    @staticmethod
    def get_model_details():
        return [
            {"name": "ct_score", "displayName": "Counter-Terrorist Score", "type": "int"},
            {"name": "t_score", "displayName": "Terrorist Score", "type": "int"},
            {"name": "map", "displayName": "Map", "type": "multi_select",
             "options": [
                 "de_inferno",
                 "de_dust2",
                 "de_nuke",
                 "de_overpass",
                 "de_mirage"
             ], },
            {"name": "bomb_planted", "displayName": "Bomb Planted", "type": "bool"},
            {"name": "ct_money", "displayName": "Counter-Terrorist Money", "type": "int"},
            {"name": "t_money", "displayName": "Terrorist Money", "type": "int"},
            {"name": "ct_health", "displayName": "Counter-Terrorist Health", "type": "int"},
            {"name": "t_health", "displayName": "Terrorist Health", "type": "int"},
            {"name": "ct_armor", "displayName": "Counter-Terrorist Armor", "type": "int"},
            {"name": "t_armor", "displayName": "Terrorist Armor", "type": "int"},
            {"name": "ct_helmets", "displayName": "Counter-Terrorist Helmets", "type": "int"},
            {"name": "t_helmets", "displayName": "Terrorist Helmets", "type": "int"},
            {"name": "ct_defuse_kits", "displayName": "Counter-Terrorist Defuse Kits", "type": "int"},
            {"name": "ct_players_alive", "displayName": "Counter-Terrorist Players Alive", "type": "int"},
            {"name": "t_players_alive", "displayName": "Terrorist Players Alive", "type": "int"},
            {"name": "ct_grenade_hegrenade", "displayName": "Counter-Terrorist Grenade HE Grenade", "type": "int"},
            {"name": "t_grenade_hegrenade", "displayName": "Terrorist Grenade HE Grenade", "type": "int"},
            {"name": "ct_grenade_flashbang", "displayName": "Counter-Terrorist Grenade Flashbang", "type": "int"},
            {"name": "t_grenade_flashbang", "displayName": "Terrorist Grenade Flashbang", "type": "int"},
            {"name": "ct_grenade_smokegrenade", "displayName": "Counter-Terrorist Grenade Smoke Grenade",
             "type": "int"},
            {"name": "t_grenade_smokegrenade", "displayName": "Terrorist Grenade Smoke Grenade", "type": "int"},
            {"name": "ct_grenade_incendiarygrenade", "displayName": "Counter-Terrorist Grenade Incendiary Grenade",
             "type": "int"},
            {"name": "t_grenade_incendiarygrenade", "displayName": "Terrorist Grenade Incendiary Grenade",
             "type": "int"},
            {"name": "ct_weapon_ak47", "displayName": "Counter-Terrorist Weapon AK-47", "type": "int"},
            {"name": "t_weapon_ak47", "displayName": "Terrorist Weapon AK-47", "type": "int"},
            {"name": "ct_weapon_awp", "displayName": "Counter-Terrorist Weapon AWP", "type": "int"},
            {"name": "t_weapon_awp", "displayName": "Terrorist Weapon AWP", "type": "int"},
            {"name": "ct_weapon_m4a1s", "displayName": "Counter-Terrorist Weapon M4A1-S", "type": "int"},
            {"name": "ct_weapon_m4a4", "displayName": "Counter-Terrorist Weapon M4A4", "type": "int"},
            {"name": "ct_weapon_deagle", "displayName": "Counter-Terrorist Weapon Desert Eagle", "type": "int"},
            {"name": "t_weapon_deagle", "displayName": "Terrorist Weapon Desert Eagle", "type": "int"}
        ]
