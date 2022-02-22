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
    name = 'Kuri_NEON'

    headers = {"Authorization": constants.API_KEY}
    r = requests.get(f'https://api2.r6stats.com/public-api/stats/{name}/pc/operators', headers=headers)
    data = r.json()

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

    attack = attack.to_json()
    defend = defend.to_json()

    collection.update_one({'username': name}, {'$set': {'attacker_stats': attack, 'defender_stats': defend}})

    attacker_ret = db.players.find_one({'username': name})['attacker_stats']
    attack_reform = pd.read_json(attacker_ret)
    print(attack_reform.head())

main()