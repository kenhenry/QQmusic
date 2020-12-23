# -*- coding: utf-8 -*-
import os
import json
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from pandas.io.json import json_normalize
from sqlalchemy.types import NVARCHAR, Float, DATE,TIME,INTEGER,TEXT
# https://github.com/kenhenry/music.git
 #显示所有列

pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
# #设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth',100)

engine = create_engine('mssql+pymssql://sa:kingdee$2018@localhost:1433/db2?charset=utf8') # ,echo = True  # echo 是否显示数据库执行过程

js ={
	'singer_name': ['周杰伦'],
	'song_name': '说好不哭（with 五月天阿信）',
	'subtitle': '',
	'album_name': '说好不哭（with 五月天阿信）',
	'singer_id': [4558],
	'singer_mid': ['0025NhlN2yWrP4'],
	'song_time_public': '2019-09-16',
	'song_type': 0,
	'language': 0,
	'song_id': 237773700,
	'song_mid': '001qvvgF38HVc4',
	'song_url': 'https://y.qq.com/n/yqq/song/001qvvgF38HVc4.html',
	'hot_comments': '',
	'lyric': '说好不哭（with 五月天阿信） - 周杰伦 (Jay Chou)\\n词：方文山\\n曲：周杰伦\\n周杰伦：\\n没有了联络 后来的生活\\n我都是听别人说\\n说你怎么了 说你怎么过\\n放不下的人是我\\n人多的时候 就待在角落\\n就怕别人问起我\\n你们怎么了 你低着头\\n护着我连抱怨都没有\\n电话开始躲 从不对我说\\n不习惯一个人生活\\n离开我以后 要我好好过\\n怕打扰想自由的我\\n都这个时候 你还在意着\\n别人是怎么怎么看我的\\n拼命解释着 不是我的错 是你要走\\n眼看着你难过 挽留的话却没有说\\n你会微笑放手 说好不哭让我走\\n阿信：\\n电话开始躲 从不对我说\\n不习惯一个人生活\\n离开我以后 要我好好过\\n怕打扰想自由的我\\n都这个时候 你还在意着\\n别人是怎么怎么看我的\\n拼命解释着 不是我的错 是你要走\\n合：\\n眼看着你难过 挽留的话却没有说\\n你会微笑放手 说好不哭让我走\\n周杰伦：\\n你什么都没有 却还为我的梦加油\\n阿信：\\n心疼过了多久\\n周杰伦：\\n过了多久\\n合：\\n还在找理由等我'
}


df = json_normalize(js)

print(df.columns)
print(df.dtypes)
# print(type(df),len(df))

# print(type(js),js)
# k=list(js.keys())
# print(type(k),k)

# list =[]
# for i in js:
#     # print(js[i])
#     list.append(js[i])
# print(list)

# df1 = pd.DataFrame.from_dict(js,columns=k,orient='index')
#
# dtypedict={'album_name':TEXT,'hot_comments':TEXT,'language':TEXT,'lyric':TEXT,'singer_id':TEXT,'singer_mid':TEXT,'singer_name':TEXT,'song_id':TEXT,'song_mid':TEXT,'song_name':TEXT,'song_time_public':TEXT,'song_type':TEXT,'song_url':TEXT,'subtitle':TEXT}
df.to_sql(name='abc', con=engine, if_exists='append',index=False) # ,dtype=dtypedict)  # 写入
#
# print(df1)