from account_stat import Account
import json
import pandas as pd
import requests
from pymongo import MongoClient
import constants

client = MongoClient(constants.MONGO_ACCOUNT)
db=client.public
collection = db.players


def get_data(name):
    # with open('stat_files/' + file) as f:
    #     data = json.load(f)
    data = db.players.find_one({'username': name})

    if data is None:
        print("Player not found")
        return None

    column_names = ["name", "ctu", "role","kills","deaths","kd","wins","losses","wl","headshots","dbnos","melee_kills","experience","playtime"]

    df = pd.DataFrame(columns = column_names)

    for i in data['operators']:
        i.pop('abilities', None)
        i.pop('badge_image', None)
        df = df.append(i,ignore_index=True)
    return df


def main():
    # headers = {"Authorization": constants.API_KEY}
    # r = requests.get("https://api2.r6stats.com/public-api/stats/Kuri_NEON/pc/operators", headers=headers)
    # data = r.json()
    name = 'Kuri_NEON'

    all_ops_df = get_data(name)

    if all_ops_df is None:
        return

    attacker_df = all_ops_df[all_ops_df['role'] == "Attacker"]
    defender_df = all_ops_df[all_ops_df['role'] == "Defender"]
    player_obj = Account(name, attacker_df, defender_df)
    print("Stats for " + player_obj.account_name)
    attack = player_obj.attacker_stats(attacker_df)
    print() 
    defend = player_obj.defender_stats(defender_df)


main()