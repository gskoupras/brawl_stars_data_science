api_token='<API_TOKEN>'

player_tag='<PLAYER_TAG>'

verbose = True

col_to_drop = ['timestamp', 'event_id', 'sum_of_trop', 'id_in_tm1']

df_columns = ['timestamp', 'event_id', 'mode', 'map','type', 'id_in_tm1',
              'pl1_tm1_brawler', 'pl1_tm1_brwlr_trop', 'pl1_tm1_brwlr_pwr',
              'pl2_tm1_brawler', 'pl2_tm1_brwlr_trop', 'pl2_tm1_brwlr_pwr',
              'pl3_tm1_brawler', 'pl3_tm1_brwlr_trop', 'pl3_tm1_brwlr_pwr',
              'pl1_tm2_brawler', 'pl1_tm2_brwlr_trop', 'pl1_tm2_brwlr_pwr',
              'pl2_tm2_brawler', 'pl2_tm2_brwlr_trop', 'pl2_tm2_brwlr_pwr',
              'pl3_tm2_brawler', 'pl3_tm2_brwlr_trop', 'pl3_tm2_brwlr_pwr',
              'tm1_win']

loc = 'data'

bat_per_map_mode = 200