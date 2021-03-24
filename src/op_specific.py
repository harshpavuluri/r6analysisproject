from genarics import *
import pandas as pd
pd.set_option("display.max_rows", None)

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
        "K/D": kd(df),
        "wins": sum_wins(df),
        "losses": sum_losses(df),
        "headshots": sum_headshots(df),
        "head_per_eng": headshots_per_eng(df),
        "wins_per_eng": wins_per_eng(df),
        "kills_per_min": kills_per_min(df),
        "experience": sum_experience(df),
        "playtime": sum_playtime(df)
    }
    col_names = ["name", "kills","deaths", "K/D" ,"wins","losses", "headshots","head_per_eng","wins_per_eng","experience","playtime"]
    final_df = pd.DataFrame(columns = col_names)
    final_df = final_df.append(temp_dict, ignore_index=True)
    return final_df

def find_player_role(df):
    role_wins = comp_wins_per_eng(df)
    role_heads = comp_head_per_eng(df)
    # print(role_wins)
    name_wins = role_wins["name"]
    val_wins = role_wins["wins_per_eng"]
    print("Wins most engagments with "+ name_wins + " operators at a " + str(round(val_wins,2)) + " rate" )
    pass

def attacker_stats(df):
    print("On attack:")
    role_list = ["Hard Breacher","Hard Breach Support","Soft Breachers","Entry Fraggers","Disrupters","Angle Watchers","Area Denial","Intel Gatherers"]
    
    hard_breach = ["Thermite" , "Hibana", "Maverick", "Ace"]
    hard_breach_supp = ["Thathcer", "Kali", "Twitch", "Maverick", "IQ"]
    soft_breach = ["Buck", "Sledge", "Zofia", "Ash", "Jackal", "Amaru"]
    entry_frag = ["Ash", "Zofia", "Jackal", "Buck", "Sledge", "IQ", "Twitch", "Blitz", "Maverick", "Nomad", "Ying", "Nøkk", "Finka"] 
    disrupt = ["Lion", "Dokkaebi", "Montagne", "Nomad", "Capitao", "Fuze", "Jackal"]
    angle_watch = ["Blackbeard", "Glaz", "Kali"]
    area_den = ["Gridlock", "Nomad", "Capitao"]
    intel_gath = ["Jackal", "Dokkaebi", "Lion", "Montagne", "IQ", "Iana"] 

    op_list =  [hard_breach, hard_breach_supp, soft_breach,entry_frag,disrupt, angle_watch, area_den, intel_gath]

    col_names = ["name", "kills","deaths","K/D", "wins","losses", "headshots","head_per_eng","wins_per_eng","experience","playtime"]
    final_df = pd.DataFrame(columns = col_names)

    for i in range(len(role_list)):
        final_df = final_df.append(role_stat(df,op_list[i],role_list[i]),ignore_index=True)
    
    find_player_role(final_df)
    print(final_df)

    pass


def defender_stats(df):
    print("On defense:")
    role_list = ["Breach Denial", "Anti-Intel", "Area Denial", "Intel Gathering", "Trappers", "Dedicated Roamers", "Support"]
    
    breah_den = ["Bandit", "Mute", "Kaid"]
    anti_int = ["Bandit", "Mute", "Kaid", "Mozzie"]
    area_den = ["Mira", "Smoke", "Goyo", "Melusi", "Castle", "Tachanka", "Aruni"]
    intel_gath = ["Valkyrie", "Echo", "Maestro", "Pulse", "Alibi", "Melusi", "Clash", "Mozzie", "Warden", "Caveira"]
    trap = ["Lesion", "Frost", "Kapkan", "Ela"]
    ded_roam = ["Caveira", "Vigil", "Oryx"]
    support = ["Jäger", "Wamai", "Rook", "Doc"]

    op_list = [breah_den, anti_int, area_den, intel_gath, trap, ded_roam, support]

    col_names = ["name", "kills","deaths","K/D", "wins","losses", "headshots","head_per_eng","wins_per_eng","experience","playtime"]
    final_df = pd.DataFrame(columns = col_names)

    for i in range(len(role_list)):
        final_df = final_df.append(role_stat(df,op_list[i],role_list[i]),ignore_index=True)
    
    find_player_role(final_df)
    print(final_df)

    pass