game_mode_types = [
    "Soccer",
    "Hoops",
    "Dropshot",
    "Hockey",
    "Rumble",
    "Heatseeker",
    "Gridiron",
]

game_map_dict = {
    "DFHStadium": "Stadium_P",
    "Mannfield": "EuroStadium_P",
    "ChampionsField": "cs_p",
    "UrbanCentral": "TrainStation_P",
    "BeckwithPark": "Park_P",
    "UtopiaColiseum": "UtopiaStadium_P",
    "Wasteland": "wasteland_s_p",
    "NeoTokyo": "NeoTokyo_Standard_P",
    "AquaDome": "Underwater_P",
    "StarbaseArc": "arc_standard_p",
    "Farmstead": "farm_p",
    "SaltyShores": "beach_P",
    "DFHStadium_Stormy": "Stadium_Foggy_P",
    "DFHStadium_Day": "stadium_day_p",
    "Mannfield_Stormy": "EuroStadium_Rainy_P",
    "Mannfield_Night": "EuroStadium_Night_P",
    "ChampionsField_Day": "cs_day_p",
    "BeckwithPark_Stormy": "Park_Rainy_P",
    "BeckwithPark_Midnight": "Park_Night_P",
    "UrbanCentral_Night": "TrainStation_Night_P",
    "UrbanCentral_Dawn": "TrainStation_Dawn_P",
    "UtopiaColiseum_Dusk": "UtopiaStadium_Dusk_P",
    "DFHStadium_Snowy": "Stadium_Winter_P",
    "Mannfield_Snowy": "eurostadium_snownight_p",
    "UtopiaColiseum_Snowy": "UtopiaStadium_Snow_P",
    "Badlands": "Wasteland_P",
    "Badlands_Night": "Wasteland_Night_P",
    "TokyoUnderpass": "NeoTokyo_P",
    "Arctagon": "ARC_P",
    "Pillars": "Labs_CirclePillars_P",
    "Cosmic": "Labs_Cosmic_V4_P",
    "DoubleGoal": "Labs_DoubleGoal_V2_P",
    "Octagon": "Labs_Octagon_02_P",
    "Underpass": "Labs_Underpass_P",
    "UtopiaRetro": "Labs_Utopia_P",
    "Hoops_DunkHouse": "HoopsStadium_P",
    "DropShot_Core707": "ShatterShot_P",
    "ThrowbackStadium": "ThrowbackStadium_P",
    "ForbiddenTemple": "CHN_Stadium_P",
    "RivalsArena": "cs_hw_p",
    "Farmstead_Night": "Farm_Night_P",
    "SaltyShores_Night": "beach_night_p",
    "NeonFields": "music_p",
    "DFHStadium_Circuit": "Stadium_Race_Day_P",
    "DeadeyeCanyon": "Outlaw_P",
    "StarbaseArc_Aftermath": "ARC_Darc_P",
    "Wasteland_Night": "Wasteland_Night_S_P",
    "BeckwithPark_GothamNight": "Park_Bman_P",
    "ForbiddenTemple_Day": "CHN_Stadium_Day_P",
    "UrbanCentral_Haunted": "Haunted_TrainStation_P",
    "ChampionsField_NFL": "BB_P",
    "ThrowbackStadium_Snowy": "ThrowbackHockey_p",
    "Basin": "Labs_Basin_P",
    "Corridor": "Labs_Corridor_P",
    "Loophole": "Labs_Holyfield_P",
    "Galleon": "Labs_Galleon_P",
    "GalleonRetro": "Labs_Galleon_Mast_P",
    "Hourglass": "Labs_PillarGlass_P",
    "Barricade": "Labs_PillarHeat_P",
    "Colossus": "Labs_PillarWings_P",
    "BeckwithPark_Snowy": "Park_Snowy_P",
    "NeoTokyo_Comic": "NeoTokyo_Toon_P",
    "UtopiaColiseum_Gilded": "UtopiaStadium_Lux_P",
    "SovereignHeights": "Street_P",
    "Hoops_TheBlock": "HoopsStreet_P",
    "Farmstead_Spooky": "Farm_HW_P",
    "ChampionsField_NikeFC": "swoosh_p",
    "ForbiddenTemple_FireAndIce": "fni_stadium_p",
    "DeadeyeCanyon_Oasis": "outlaw_oasis_p",
    "EstadioVida_Dusk": "ff_dusk_p",
    "Mannfield_Dusk": "eurostadium_dusk_p",
    "Farmstead_Pitched": "farm_grs_p",
    "Farmstead_Upsidedown": "farm_hw_p",
    "Wasteland_Pitched": "wasteland_grs_p",
    "Neotokyo_Hacked": "neotokyo_hax_p",
}

map_types = list(game_map_dict.keys())

match_length_types = ["5 Minutes", "10 Minutes", "20 Minutes", "Unlimited"]

max_score_types = [
    "Unlimited",
    "1 Goal",
    "3 Goals",
    "5 Goals",
]

overtime_mutator_types = ["Unlimited", "+5 Max, First Score", "+5 Max, Random Team"]

series_length_mutator_types = [
    "Unlimited",
    "3 Games",
    "5 Games",
    "7 Games",
]

game_speed_mutator_types = ["Default", "Slo-Mo", "Time Warp"]

ball_max_speed_mutator_types = ["Default", "Slow", "Fast", "Super Fast"]

ball_type_mutator_types = ["Default", "Cube", "Puck", "Basketball"]

ball_weight_mutator_types = ["Default", "Light", "Heavy", "Super Light"]

ball_size_mutator_types = ["Default", "Small", "Large", "Gigantic"]

ball_bounciness_mutator_types = ["Default", "Low", "High", "Super High"]

boost_amount_mutator_types = [
    "Default",
    "Unlimited",
    "Recharge (Slow)",
    "Recharge (Fast)",
    "No Boost",
]

rumble_mutator_types = [
    "None",
    "Default",
    "Slow",
    "Civilized",
    "Destruction Derby",
    "Spring Loaded",
    "Spikes Only",
    "Spike Rush",
]

boost_strength_mutator_types = ["1x", "1.5x", "2x", "10x"]

gravity_mutator_types = ["Default", "Low", "High", "Super High"]

demolish_mutator_types = [
    "Default",
    "Disabled",
    "Friendly Fire",
    "On Contact",
    "On Contact (FF)",
]

respawn_time_mutator_types = [
    "3 Seconds",
    "2 Seconds",
    "1 Second",
    "Disable Goal Reset",
]

existing_match_behavior_types = [
    "Restart",
    "Restart If Different",
    "Continue And Spawn",
]
