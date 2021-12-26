
import sys
import os
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)
  
# now we can import the module in the parent
# directory.
from account_stat import Account
import json
import pandas as pd
import numpy as np

def get_data(file):
    with open('stat_files/' + file) as f:
        data = json.load(f)

    column_names = ["name", "ctu", "role","kills","deaths","kd","wins","losses","wl","headshots","dbnos","melee_kills","experience","playtime"]

    df = pd.DataFrame(columns = column_names)

    for i in data['operators']:
        i.pop('abilities', None)
        i.pop('badge_image', None)
        df = df.append(i,ignore_index=True)
    return df


def test_attack():
    all_ops_df = get_data('ops_kuri.json')
    attacker_df = all_ops_df[all_ops_df['role'] == "Attacker"]
    # defender_df = all_ops_df[all_ops_df['role'] == "Defender"]
    kuri_obj = Account("Kuri_NEON")
    attack = kuri_obj.attacker_stats(attacker_df)
    schema_types = {
            "name": np.dtype('O'),
            "kills": np.dtype('int64'),
            "deaths": np.dtype('int64'),
            "K/D": np.dtype('float64'),
            "wins": np.dtype('int64'),
            "losses": np.dtype('int64'),
            "headshots": np.dtype('int64'),
            "head_per_eng": np.dtype('float64'),
            "wins_per_eng": np.dtype('float64'),
            "kills_per_min": np.dtype('float64'),
            "experience": np.dtype('int64'),
            "playtime": np.dtype('int64')
        }
    attack_types = kuri_obj.attacker_roles.dtypes.to_dict()
    # print(attack_types)
    assert attack_types == schema_types
def test_defend():
    all_ops_df = get_data('ops_kuri.json')
    defender_df = all_ops_df[all_ops_df['role'] == "Defender"]
    kuri_obj = Account("Kuri_NEON")
    defend = kuri_obj.defender_stats(defender_df)
    schema_types = {
            "name": np.dtype('O'),
            "kills": np.dtype('int64'),
            "deaths": np.dtype('int64'),
            "K/D": np.dtype('float64'),
            "wins": np.dtype('int64'),
            "losses": np.dtype('int64'),
            "headshots": np.dtype('int64'),
            "head_per_eng": np.dtype('float64'),
            "wins_per_eng": np.dtype('float64'),
            "kills_per_min": np.dtype('float64'),
            "experience": np.dtype('int64'),
            "playtime": np.dtype('int64')
        }
    defend_types = kuri_obj.defender_roles.dtypes.to_dict()
    # print(attack_types)
    assert defend_types == schema_types
    pass