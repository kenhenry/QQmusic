# -*- coding: utf-8 -*-
import json
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mssql+pymssql://sa:kingdee$2018@localhost:1433/MusicDB?charset=utf8') # ,echo = True  # echo 是否显示数据库执行过程

with open('F:\Git_Project\music/music_detail','r',encoding='utf-8') as f:
    j = 0
    js_list =[]
    for js in f:
        js = json.loads(js)
        for v in js:
            js[v] = str(js[v])
        # print(js)
        js_list.append(js)

        # j = j +1
        # if j==5000:
        #     # print(i)
        #     f.close()
        #     break

result = pd.DataFrame()
for js in js_list:
    df = pd.json_normalize(js)
    df = df[['singer_name', 'song_name', 'subtitle', 'album_name', 'singer_id', 'singer_mid', 'song_time_public', 'song_type', 'language', 'song_id', 'song_mid', 'song_url']]
    result = result.append(df)

result.to_sql(name='music', con=engine, if_exists='append',index=False) #,dtype=dtypedict)  # 写入


