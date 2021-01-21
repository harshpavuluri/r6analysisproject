"""
This file will generate stats on generaic playstyle will typically try to measure aim.
To measure this, I believe that headshot rate is important. Since headshots with any gun
will result in a kill, we can use a headshots as a point of reference to measure aim

"""
def sum_deaths(df):
    return df['deaths'].sum()

def sum_kills(df):
    return df['kills'].sum()

def sum_headshots(df):
    return df['headshots'].sum()

def headshots_per_eng(df):
    engagaments = (sum_kills(df) + sum_deaths(df)) * 0.95 # 5% is taken off here for non engagements deaths (Suicides, traps, etc)
    headshots = sum_headshots(df)
    return headshots / engagaments

def wins_per_eng(df):
    engagaments = (sum_kills(df) + sum_deaths(df)) * 0.95 # 5% is taken off here for non engagements deaths (Suicides, traps, etc)
    kills_trim = sum_kills(df) * 0.95 # Error like last variable
    return kills_trim / engagaments


def runner(generaic_ops_df):
    print("Headshots per Engagment: " + str(headshots_per_eng(generaic_ops_df)))
    print("Wins per Engagment: " + str(wins_per_eng(generaic_ops_df)))

    pass
