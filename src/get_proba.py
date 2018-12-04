from DataPreparation import *
import pandas as pd
import numpy as np

def get_proba(username, model):
    url = 'https://www.instagram.com/%s/' % username
    get_info(url)
    get_new_features(url)
    one_user = []
    for item in get_info(url):
        one_user.append(item)
    for feature in get_new_features(url):
        one_user.append(feature)
    one_user_df = pd.DataFrame(np.array(one_user).reshape(1,-1))
    one_user_df['num_followers_float'] = one_user_df.apply(lambda row: float(row[3].replace('k', 'e3').replace('m', 'e6')), axis=1)
    one_user_df['following_follower_ratio'] = float(one_user_df[4]) / (float(one_user_df['num_followers_float']) +1)
    one_user_df = one_user_df.drop(8, axis = 1)
    one_user_df.iloc[0,5] = [1 if one_user_df.iloc[0,5] == 'True' else 0]
    one_user_df.iloc[0,6] = [1 if one_user_df.iloc[0,6] == 'True' else 0]
    one_user_df.iloc[0,7] = [1 if one_user_df.iloc[0,7] == 'True' else 0]
    one_user_df.iloc[:,[2,4,5,6,7,8,9]]
    one_user_pred_proba = model.predict_proba(one_user_df.iloc[:,[2,4,5,6,7,8,9]])[:,1][0]
    one_user_df['prob_fake'] = one_user_pred_proba
    return one_user_df

