# -*- coding: utf-8 -*-
import json
import pandas as pd
from sqlalchemy import create_engine
from pandas.io.json import json_normalize

engine = create_engine('mssql+pymssql://sa:kingdee$2018@localhost:1433/MusicDB?charset=utf8') # ,echo = True  # echo 是否显示数据库执行过程

with open('E:/00Git_Project/QQmusic/music_detail','r',encoding='utf-8') as f:
    j = 0
    for js in f:
        js = json.loads(js)
        for v in js:
            js[v] = str(js[v])
        df = json_normalize(js)
        df = df[['singer_name', 'song_name', 'subtitle', 'album_name', 'singer_id', 'singer_mid', 'song_time_public',
                 'song_type', 'language', 'song_id', 'song_mid', 'song_url']]
        df.to_sql(name='music', con=engine, if_exists='append', index=False)    # 写入

        j = j +1
        print(j)
        if j==489860:
        # if j==50:
            # print(i)
            f.close()
            break
print('ok')



