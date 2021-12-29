from flask import Flask, jsonify, request, make_response
from flask.wrappers import Request
import json
import pandas as pd
import os, sys
from account_stat import Account


APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STAT_FILES = os.path.join(APP_ROOT, 'stat_files')

app = Flask(__name__)

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

@app.route('/')
def home():
    return 'R6 Analysis project API'

@app.route('/stats/<account_name>', methods= ['GET'])
def stats(account_name):
    if request.method == 'GET':
        df = None
        
        for file in os.listdir(APP_STAT_FILES):
            if account_name.lower() in file:
                account_name = account_name.lower()
                df = get_data(f'{account_name}_ops.json')
                break
        if df is not None:
            return df.to_json()
        else: 
            return f'{account_name} not found'

@app.route('/stats/<account_name>/<role>', methods= ['GET'])
def stats_role(account_name, role):
    if request.method == 'GET':
        df = None
        if role == "attacker" or role == "defender":
            account_name = account_name.lower()
            df = get_data(f'{account_name}_ops.json')
            attacker_df = df[df['role'] == "Attacker"]
            defender_df = df[df['role'] == "Defender"]
            temp_obj = Account(account_name, attacker_df, defender_df)
            if role == "attacker":
                attack = temp_obj.attacker_stats(attacker_df)
                return attack.to_json()
            elif role == "defender":
                defend = temp_obj.defender_stats(defender_df)
                return defend.to_json()
        else:
            return f'{role} is not found' 


# @app.route('/create/<account_name>', methods= ['POST'])
# def create(account_name):
#     if request.method == 'POST':
#         account_name = account_name.lower()
#         df = get_data(f'{account_name}_ops.json')
#         if df is not None:

