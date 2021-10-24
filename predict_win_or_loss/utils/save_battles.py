import numpy as np
import pandas as pd
from datetime import datetime


def save_battles(df, loc='data', verbose=True):
    
    # Get current time (up to the second)
    now = datetime.now()
    current_time = now.strftime('%m_%d_%Y_%H_%M_%S')
    
    # Final key to use
    key = loc + '/' + 'battles_' + current_time + '.csv'
    
    df.to_csv(key)
    
    if verbose:
        print('File saved in location: {}'.format(key))