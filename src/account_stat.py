import pandas as pd
pd.set_option("display.max_rows", None)

class Account:
    '''
    Class variables:
    defender_roles: dataframe
    attacker_roles: dataframe

    Functions:
    __init__: Initiate Class
    role_stat: Takes a dataframe and a list of operators and returns a dataframe with the stats of the operators in the list
    find_player_role: Takes a dataframe and the most successful role a account plays
    attacker_stats: Takes a dataframe and returns a dataframe of attacker roles
    defender_stats: Takes a dataframe and returns a dataframe of defender roles
    '''
    def __init__(self):

        pass

    def __sum_deaths(self,df):
        return df['deaths'].sum()

    def __sum_kills(self,df):
        return df['kills'].sum()

    def __sum_headshots(self,df):
        return df['headshots'].sum()

    def __sum_playtime(self,df):
        return df['playtime'].sum()

    def __sum_experience(self,df):
        return df['experience'].sum()

    def __sum_wins(self,df):
        return df['wins'].sum()

    def __sum_losses(self,df):
        return df['losses'].sum()

    def __kd(self,df):
        return self.__sum_kills(df) / self.__sum_deaths(df)

    def __headshots_per_eng(self,df):
        engagaments = (self.__sum_kills(df) + self.__sum_deaths(df)) * 0.95 # 5% is taken off here for non engagements deaths (Suicides, traps, etc)
        headshots = self.__sum_headshots(df)
        return headshots / engagaments

    def __wins_per_eng(self,df):
        engagaments = (self.__sum_kills(df) + self.__sum_deaths(df)) * 0.95 # 5% is taken off here for non engagements deaths (Suicides, traps, etc)
        kills_trim = self.__sum_kills(df) * 0.95 # Error like last variable
        return kills_trim / engagaments

    # comparisons 
    def __comp_wins_per_eng(self,df):
        col = df["wins_per_eng"]
        # print(col)
        max_ind = col.idxmax()
        # print(max_ind)
        # print(df.loc[max_ind])
        return df.loc[max_ind]

    def __kills_per_min(self,df):
        kills = self.__sum_kills(df) 
        minu = self.__sum_playtime(df) / 60
        return kills/minu

    def __comp_head_per_eng(self,df):
        pass


    # def runner(self,generaic_ops_df):
    #     print("Headshots per Engagment: " + str(self.headshots_per_eng(generaic_ops_df)))
    #     print("Wins per Engagment: " + str(self.wins_per_eng(generaic_ops_df)))

    #     pass

    def role_stat(self,df_role, op_list, name_op):
        '''
        This function takes a dataframe and a list of operators and returns a dataframe with the stats of the operators in the list
        Input: dataframe, list of operators, name of the role
        Output: dataframe
        '''
        column_names = ["name", "ctu", "role","kills","deaths","kd","wins","losses","wl","headshots","dbnos","melee_kills","experience","playtime"]
        df = pd.DataFrame(columns = column_names)
        for i in op_list:
            # print(df_role.loc[df_role['name'] == i])
            df = df.append(df_role.loc[df_role['name'] == i],ignore_index=True)
        
        temp_dict = {
            "name": name_op,
            "kills": self.__sum_kills(df),
            "deaths": self.__sum_deaths(df),
            "K/D": self.__kd(df),
            "wins": self.__sum_wins(df),
            "losses": self.__sum_losses(df),
            "headshots": self.__sum_headshots(df),
            "head_per_eng": self.__headshots_per_eng(df),
            "wins_per_eng": self.__wins_per_eng(df),
            "kills_per_min": self.__kills_per_min(df),
            "experience": self.__sum_experience(df),
            "playtime": self.__sum_playtime(df)
        }
        col_names = ["name", "kills","deaths", "K/D" ,"wins","losses", "headshots","head_per_eng","wins_per_eng","experience","playtime"]
        final_df = pd.DataFrame(columns = col_names)
        final_df = final_df.append(temp_dict, ignore_index=True)
        return final_df

    def find_player_role(self,df):
        '''
        This function takes a dataframe and the most successful role a account plays
        Input: dataframe
        Output: string
        '''
        role_wins = self.__comp_wins_per_eng(df)
        role_heads = self.__comp_head_per_eng(df)
        # print(role_wins)
        name_wins = role_wins["name"]
        val_wins = role_wins["wins_per_eng"]
        print("Wins most engagments with "+ name_wins + " operators at a " + str(round(val_wins,2)) + " rate" )
        return name_wins
        pass

    def attacker_stats(self,df):
        '''
        This function takes a dataframe and returns a dataframe of attacker roles
        input: dataframe
        output: dataframe
        '''
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
            final_df = final_df.append(self.role_stat(df,op_list[i],role_list[i]),ignore_index=True)
        
        self.find_player_role(final_df)
        print(final_df)
        self.attacker_roles = final_df
        pass


    def defender_stats(self,df):
        '''
        This function takes a dataframe and returns a dataframe of defender roles
        input: dataframe
        output: dataframe
        '''
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
            final_df = final_df.append(self.role_stat(df,op_list[i],role_list[i]),ignore_index=True)
        
        self.find_player_role(final_df)
        print(final_df)
        self.defender_roles = final_df
        pass