from account_stat import Account

import json
import pandas as pd

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


def main():
    all_ops_df = get_data('ops_kuri.json')
    attacker_df = all_ops_df[all_ops_df['role'] == "Attacker"]
    defender_df = all_ops_df[all_ops_df['role'] == "Defender"]
    kuri_obj = Account("Kuri_NEON", attacker_df, defender_df)
    print("Stats for " + kuri_obj.account_name)
    attack = kuri_obj.attacker_stats(attacker_df)
    print() 
    defend = kuri_obj.defender_stats(defender_df)

main()