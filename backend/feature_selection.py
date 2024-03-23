#from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

nba_teams = teams.get_teams()

def numerical_to_categorical(data, col):
    _, bins, _ = plt.hist(data[col], bins=10)
    categorical_arr = []
    for val in data[col]:
        for i in range(10):
            if bins[i] <= val < bins[i+1]:
                categorical_arr.append(i+1)
                break

            elif val >= bins[10]:
                categorical_arr.append(10)
                break
    data[col] = categorical_arr
    return data

def get_team_data_by_game(team):
    user_team = [team_dict for team_dict in nba_teams if team_dict['full_name'] == team][0]
    team_id = user_team['id']

    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games = gamefinder.get_data_frames()[0]
    return games[:100]


def binary_encoding(data, truth_label="W"):
    binary_col = []
    for val in data["WL"]:
        if val == truth_label:
            binary_col.append(1)
        else:
            binary_col.append(0)
    data['WL'] = binary_col
    return data


    
def marginal_probability(data, col, x=True):
    # Calculating Marginal Probabilities  
    if x:
        df_columns=["x", "P(X=x)"] 
    else:
         df_columns=["y", "P(Y=y)"] 
    margina_prob_df = []
    for val in data[col].unique():
        val_count = 0
        for entry in data[col]:
            if entry == val:
                val_count += 1
        margina_prob_df.append([val, val_count/len(data[col])])
    margina_prob_df = pd.DataFrame(margina_prob_df, columns=df_columns)
    return margina_prob_df

def mutual_information(data, col, x_prob_dist, y_prob_dist, y="WL"):
    # Compute Joint Probabilities
    x_arr, y_arr = data[col], data[y]
    joint_probabilities = data.groupby([x_arr, y_arr]).size() / len(data)
    joint_probabilities = joint_probabilities.reset_index(name='P(' + ', '.join(['x', 'y']) + ')')
    joint_probabilities = joint_probabilities.rename(columns={joint_probabilities.columns[0]: "x", joint_probabilities.columns[1]: 'y'})

    # Compute Mutual Info
    mutual_info = 0
    for x_val in x_prob_dist["x"]:
        # Find p(x)
        x_data = x_prob_dist[x_prob_dist['x']==x_val]
        p_x = x_data['P(X=x)']
        p_x = p_x.iloc[0]

        # Find p(y)
        for y_val in y_prob_dist["y"]:
            y_data = y_prob_dist[y_prob_dist['y']==y_val]
            p_y = y_data['P(Y=y)']
            p_y = p_y.iloc[0]

            # Find p(x, y)
            x_y_data = joint_probabilities[joint_probabilities['x']==x_val]
            x_y_data = joint_probabilities[joint_probabilities['y']==y_val]
            p_x_y = x_y_data['P(x, y)']
            p_x_y = p_x_y.iloc[0]

            mutual_info = mutual_info + (p_x_y * np.log(p_x_y/(p_x * p_y)))
    return round(mutual_info, 3)



def main():
    team = "Boston Celtics"
    team_data = get_team_data_by_game(team.title())



    # Discretize continuous data for mutual information calculation
    continuous_cols = ["FG_PCT", "FG3_PCT", "FT_PCT"]
    for col in continuous_cols:
        team_data = numerical_to_categorical(team_data, col)
    team_data = binary_encoding(team_data)

    potential_model_features = ['MIN', 'PTS', 'FGM', 'FGA', 'FG_PCT',
       'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB',
       'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PLUS_MINUS']
    
    prob_y = marginal_probability(team_data, col='WL', x=False)

    mutual_info_df = []
    for feature in potential_model_features:
        prob_x = marginal_probability(team_data, col=feature)
        mutual_info = mutual_information(team_data, feature, prob_x, prob_y)
        mutual_info_df.append([feature, mutual_info])
    mutual_info_df = pd.DataFrame(mutual_info_df, columns=["feature", "mutual information"])
    mutual_info_df = mutual_info_df.sort_values(['mutual information'], ascending=False)
    mutual_info_df = mutual_info_df.reset_index()
    del mutual_info_df['index']
    print(mutual_info_df)






    


if __name__ == "__main__":
    main()




