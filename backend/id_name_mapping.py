#from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
import pandas as pd

# Nikola Jokić
#career = playercareerstats.PlayerCareerStats(player_id='203999') 
player_lst = players.get_active_players()
# pandas data frames (optional: pip install pandas)
#career.get_data_frames()[0]
def scrape_player_lst(player_list):
    # Create main dictionary
    main_df = {}

    # Initialize keys in main dictionary
    for key in player_list[0].keys():
        main_df[key] = []

    # Scrape through the list of dictionaries and add that info to the main df
    for player_dict in player_list:
        for key in player_list[0].keys():
            main_df[key].append(player_dict[key])

    main_df = pd.DataFrame.from_dict(main_df)
    del main_df['is_active']

    return main_df



player_lst = players.get_active_players()
player_df = scrape_player_lst(player_lst)


def get_id_from_name(name, df=player_df):
    for name_index, name_value in enumerate(df['full_name']):
        if name_value == name:
            return df['id'][name_index]
        
def get_name_from_id(id, df):
    for id_index, id_val in enumerate(df['id']):
        if id_val == id:
            return df['full_name'][id_index]

