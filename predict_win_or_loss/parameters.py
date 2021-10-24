api_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhiZjBiYzcyLTc5NTMtNDRmMS1hM2EyLWZlMTNhYmVlZTRhMyIsImlhdCI6MTYyOTU1MjU4Niwic3ViIjoiZGV2ZWxvcGVyL2VkMWNiZGE0LTY2MGMtNzlhNy1mYmI4LTZkOTc5ODA2ODM3ZSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMjA1LjI1MS4yMzMuMTc4IiwiMjA1LjI1MS4yMzMuMTgzIiwiNTQuMjM5LjYuMTkwIiwiNzcuMTAzLjEyOS42NiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.OZDg_pzUBkxman0FPaTYnlQil28mieprBst8n6dJ3MA50H3Mjqbe6K0D2i7xNA8DP2FtAlPXO11ycC_GOTNU5A"


api_token_old='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjU0MTcyMjJkLTNlYjYtNDAzMC05MjgxLWIxOGFiYjAzNmZhYiIsImlhdCI6MTYyMzQ5Njg3Nywic3ViIjoiZGV2ZWxvcGVyL2VkMWNiZGE0LTY2MGMtNzlhNy1mYmI4LTZkOTc5ODA2ODM3ZSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNzcuMTAzLjEyOS42NiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.RPFpMBronAole4dTnD6H0ydUmGxwmLOlaVF4qZMC3d1gDpqFQXxcHCveyjBlpZ28BrG69iHSc8sn2hiAD26lYA'

player_tag='YJL29QGYQ'

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

brawler_columns = ['pl1_tm1_brawler', 'pl2_tm1_brawler', 'pl3_tm1_brawler', 
                   'pl1_tm2_brawler', 'pl2_tm2_brawler', 'pl3_tm2_brawler']

loc = 'data'

bat_per_map_mode = 200