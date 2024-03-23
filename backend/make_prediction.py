import pandas as pd
import numpy as np
from tensorflow import keras 
from keras.models import load_model

team_data = pd.read_csv("name_team_data.csv")

name_abbr_map = {
    "Atlanta Hawks": 'ATL',
    "Broklyn Nets": "BKN",
    "Boston Celtics": "BOS",
    "Charlotte Hornets": "CHA",
    "Chicago Bulls": "CHI",
    "Clevland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Lakers": "LAL",
    "Los Angeles Clippers": "LAC",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOR",
    "New York Knicks": "NYK",
    "Oklahoma Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHX",
    "Portland Trailblazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio": "SAS",
    "Toronot Raptors": "TOR",
    "Utah Jazz": "UTA",
    "Washington Wizards": "WAS"
  }


scaler_dict = {'PTS': [112.821, 14.113856985246803],
 'FGM': [41.50066666666667, 5.833980878344467],
 'FGA': [88.051, 8.187209475761568],
 'FG_PCT': [0.4719136378792931, 0.0554606662951821],
 'FG3M': [12.515333333333333, 3.89167036402394],
 'FG3A': [34.68233333333333, 6.8696012418642045],
 'FG3_PCT': [0.3598139379793264, 0.08475789850854029],
 'FTM': [17.304333333333332, 5.853009017211195],
 'FTA': [22.219333333333335, 7.019346566613037],
 'FT_PCT': [0.7789426284189459, 0.10046531190728024],
 'OREB': [10.586666666666666, 3.8444534360845397],
 'DREB': [32.74033333333333, 5.538553351031497],
 'REB': [43.327, 6.804170608286264],
 'AST': [25.94333333333333, 5.346661471319171],
 'STL': [7.4976666666666665, 2.9104400392762297],
 'BLK': [5.111, 2.5728089059754646],
 'TOV': [13.152, 3.9238878679187557],
 'PF': [19.242333333333335, 4.237641783927576],
 'PLUS_MINUS': [-0.11386666666666649, 15.189584843423322]}



def synthesize_data(data):
  synthetic_data = []
  for col in data.columns:
    synthetic_data.append(np.mean(data[col]))
  np.array(synthetic_data)
  return synthetic_data


def scale_synthetic_data(row):
  new_row = []
  i = 0
  for key in scaler_dict.keys():
    scaled_val = (row[i] - scaler_dict[key][0]) / scaler_dict[key][1]
    new_row.append(scaled_val)
    i+=1
  return new_row


def make_pred(team_1, team_2):
  model = load_model("path/to/your/saved_model.h5")
   # Find  games where they played against each other
  all_data = pd.read_csv("/content/name_team_data.csv")
  del all_data["Unnamed: 0"]

  team_1_abbr = name_abbr_map[team_1]
  team_2_abbr = name_abbr_map[team_2]
  team_1_data = all_data[all_data['MATCHUP'].str[:3].eq(team_1_abbr) | all_data['MATCHUP'].str[:2].eq(team_1_abbr[:-1])]

  team_1_and_team_2_data = team_1_data[team_1_data["MATCHUP"].str[-3:].eq(team_2_abbr) | team_1_data["MATCHUP"].str[-2:].eq(team_2_abbr[:-1])]

  model_features = ['PTS', 'FGM', 'FGA', 'FG_PCT',
       'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB',
       'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PLUS_MINUS', 'WL']
  
  team_1_and_team_2_data = team_1_and_team_2_data[model_features[:-1]]
  synthetic_data = synthesize_data(team_1_and_team_2_data)
  synthetic_data_scaled = scale_synthetic_data(synthetic_data)

  synthetic_data_scaled = np.array([synthetic_data_scaled])

  prediction = model.predict(synthesize_data)
  prediction = prediction[0, 0]

  if prediction > 0.5:
    return 1
  else:
    return 2

  



if __name__ == "__main__":
    make_pred('Boston Celtics', "Dallas Mavericks")