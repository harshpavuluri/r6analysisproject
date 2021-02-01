from json_format_op import all_ops_df
from op_specific import attacker_stats
from op_specific import defender_stats

def main():
    attacker_df = all_ops_df[all_ops_df['role'] == "Attacker"]
    defender_df = all_ops_df[all_ops_df['role'] == "Defender"]

    attack = attacker_stats(attacker_df)
    # defend = defender_stats(defender_df)


main()