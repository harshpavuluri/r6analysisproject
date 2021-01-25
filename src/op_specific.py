from genarics import *
import pandas as pd

def role_stat(df_role, op_list, name_op):

    column_names = ["name", "ctu", "role","kills","deaths","kd","wins","losses","wl","headshots","dbnos","melee_kills","experience","playtime"]
    df = pd.DataFrame(columns = column_names)
    for i in op_list:
        # print(df_role.loc[df_role['name'] == i])
        df = df.append(df_role.loc[df_role['name'] == i],ignore_index=True)
    
    temp_dict = {
        "name": name_op,
        "kills": sum_kills(df),
        "deaths": sum_deaths(df),
        "wins": sum_wins(df),
        "losses": sum_losses(df),
        "headshots": sum_headshots(df),
        "head_per_eng": headshots_per_eng(df),
        "wins_per_eng": wins_per_eng(df),
        "experience": sum_experience(df),
        "playtime": sum_playtime(df)
    }
    col_names = ["name", "kills","deaths", "wins","losses", "headshots","head_per_eng","wins_per_eng","experience","playtime"]
    final_df = pd.DataFrame(columns = col_names)
    final_df = final_df.append(temp_dict, ignore_index=True)
    return final_df

def attacker_stats(df):
    role_list = ["Hard Breach", "Vertical Operators", "True Fraggers", "Anti-Roamers", "Support Operators"]
    
    hard_breach = ["Thermite" , "Hibana", "Maverick", "Ace"]
    vert_ops = ["Buck" , "Sledge", "Glaz", "Fuze", "Blackbeard"]
    true_frags = ["Ash", "Zofia", "Amaru", "Nøkk", "Iana"]
    anti_roam = ["Jackal" , "Lion", "Dokkaebi", "Nomad", "Gridlock", "Zero"]
    supp_ops = ["Capitao" , "Ying", "Gridlock", "Blitz", "Montagne", "Kali", "Thatcher", "Twitch", "IQ", "Finka", "Ying"]
    
    op_list =  [hard_breach, vert_ops, true_frags,anti_roam,supp_ops]

    col_names = ["name", "kills","deaths", "wins","losses", "headshots","head_per_eng","wins_per_eng","experience","playtime"]
    final_df = pd.DataFrame(columns = col_names)

    for i in range(len(role_list)):
        final_df = final_df.append(role_stat(df,op_list[i],role_list[i]),ignore_index=True)
    

    print(final_df.head())

    pass


def defender_stats(df):
    role_list = ["Roamers", "Anchors", "Lurkers", "Wall Denial"]
    
    roam = ["Jager" , "Caviera" , "Alibi", "Ela", "Vigil", "Melusi", "Oryx"]
    anchor = ["Maestro", "Rook" , "Doc", "Echo", "Mira", "Castle", "Smoke", "Tachanka", "Clash"]
    lurkers = ["Lesion" , "Valkyrie", "Mozzie", "Wamai", "Pulse", "Frost", "Goyo"]
    wall_den = ["Mute", "Bandit" , "Kaid", "Aruni", "Kapkan"]

    op_list = [roam, anchor, lurkers, wall_den]

    col_names = ["name", "kills","deaths", "wins","losses", "headshots","head_per_eng","wins_per_eng","experience","playtime"]
    final_df = pd.DataFrame(columns = col_names)

    for i in range(len(role_list)):
        final_df = final_df.append(role_stat(df,op_list[i],role_list[i]),ignore_index=True)
    

    print(final_df.head())

    pass