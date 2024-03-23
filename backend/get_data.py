from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

model_features = ['PTS', 'FGM', 'FGA', 'FG_PCT',
       'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB',
       'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PLUS_MINUS', 'WL']

nba_teams = teams.get_teams()

def get_team_data_by_game(index):
    team_selected = nba_teams[index]
    team_id = team_selected['id']

    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games = gamefinder.get_data_frames()[0]
    return games[:100]


team_names = []
user_team = [team_dict for team_dict in nba_teams]

for team_dict in user_team:
    team_names.append(team_dict['full_name'])

team_data = get_team_data_by_game(0)
for i in range(1, 30):
    new_data = get_team_data_by_game(i)
    team_data = pd.concat([team_data, new_data], ignore_index=True)
team_data = team_data[['MATCHUP'] + model_features]
save_path = "/Users/callihanbertley/Downloads/name_team_data.csv"
team_data.to_csv(save_path)
print(f"combined team data saved to {save_path}")