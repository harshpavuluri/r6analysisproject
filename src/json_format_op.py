import json
import pandas as pd

def main():
  with open('stat_files/ops_avo.json') as f:
    data = json.load(f)

  # print(data)
  # print(json.dumps(data, indent = 4, sort_keys=False))

  # print(data['operators'][1])

  # print(len(data['operators']))

  column_names = ["name", "ctu", "role","kills","deaths","kd","wins","losses","wl","headshots","dbnos","melee_kills","experience","playtime"]

  df = pd.DataFrame(columns = column_names)

  for i in data['operators']:
      i.pop('abilities', None)
      i.pop('badge_image', None)
      df = df.append(i,ignore_index=True)

  return df



  pass 

all_ops_df = main()

# print(attacker_df)
# print(defender_df)