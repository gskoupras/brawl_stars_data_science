import numpy as np
import pandas as pd


def remove_duplicate_battles(df, verbose):
    '''
    This function takes as input a dataframe with all the battles that were just scanned by the API Call 
    and removes all the potential duplicates that could occur due to top players playing together. 
    
    '''
    
    # Get sum of trophies for identifier
    df['sum_of_trop'] = df['pl1_tm1_brwlr_trop'] + df['pl2_tm1_brwlr_trop'] + df['pl3_tm1_brwlr_trop'] + \
                        df['pl1_tm2_brwlr_trop'] + df['pl2_tm2_brwlr_trop'] + df['pl3_tm2_brwlr_trop']
    
    # Cast strings for identifier of unique battles
    df['timestamp'] = df['timestamp'].astype(str)
    df['event_id'] = df['event_id'].astype(str)
    df['sum_of_trop'] = df['sum_of_trop'].astype(str)
    
    # Create identifier of unique battles
    df['unq_battle_id'] = df['timestamp'] + '_' + df['event_id'] + '_' + df['sum_of_trop']
    
    # Remove duplicate battles
    len_bef = len(df)
    df = df.drop_duplicates(subset='unq_battle_id', keep='first')
    len_af = len(df)
    if verbose:
        print('{} out of {} Battles removed. {} Battles remaining.'. format(len_bef-len_af, len_bef, len_af))
    
    return df