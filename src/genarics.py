"""
This file will generate stats on generaic playstyle will typically try to measure aim.
To measure this, I believe that headshot rate is important. Since headshots with any gun
will result in a kill, we can use a headshots as a point of reference to measure aim

"""
from pandas import *
# caluclations
def sum_deaths(df):
    return df['deaths'].sum()

def sum_kills(df):
    return df['kills'].sum()

def sum_headshots(df):
    return df['headshots'].sum()

def sum_playtime(df):
    return df['playtime'].sum()

def sum_experience(df):
    return df['experience'].sum()

def sum_wins(df):
    return df['wins'].sum()

def sum_losses(df):
    return df['losses'].sum()

def kd(df):
    return sum_kills(df) / sum_deaths(df)

def headshots_per_eng(df):
    engagaments = (sum_kills(df) + sum_deaths(df)) * 0.95 # 5% is taken off here for non engagements deaths (Suicides, traps, etc)
    headshots = sum_headshots(df)
    return headshots / engagaments

def wins_per_eng(df):
    engagaments = (sum_kills(df) + sum_deaths(df)) * 0.95 # 5% is taken off here for non engagements deaths (Suicides, traps, etc)
    kills_trim = sum_kills(df) * 0.95 # Error like last variable
    return kills_trim / engagaments

# comparisons 
def comp_wins_per_eng(df):
    col = df["wins_per_eng"]
    # print(col)
    max_ind = col.idxmax()
    # print(max_ind)
    # print(df.loc[max_ind])
    return df.loc[max_ind]

def kills_per_min(df):
    kills = sum_kills(df) 
    minu = sum_playtime(df) / 60
    return kills/minu

def comp_head_per_eng(df):
    pass


def runner(generaic_ops_df):
    print("Headshots per Engagment: " + str(headshots_per_eng(generaic_ops_df)))
    print("Wins per Engagment: " + str(wins_per_eng(generaic_ops_df)))

    pass
