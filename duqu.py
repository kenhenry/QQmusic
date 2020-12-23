# -*- coding: utf-8 -*-
import os
import json
import pandas as pd
from sqlalchemy import create_engine
from pandas.io.json import json_normalize

engine = create_engine('mssql+pymssql://sa:kingdee$2018@localhost:1433/db2?charset=utf8') # ,echo = True  # echo 是否显示数据库执行过程

with open('E:/00Git_Project/QQmusic/music_detail','r',encoding='utf-8') as f:
    j = 0
    js_list =[]
    for i in f:
        i = json.loads(i)
        js_list.append(i)

        j = j +1
        if j==5:
            # print(i)
            f.close()
            break
# print(js_list)
result = pd.DataFrame()
for js in js_list:
    df = json_normalize(js)
    df = df[['album_name', 'language', 'lyric', 'singer_id','singer_mid', 'singer_name', 'song_id', 'song_mid', 'song_name','song_time_public', 'song_type', 'song_url', 'subtitle']]
    # df_all = pd.concat([df_all,df])
    result = result.append(df)

print(result)
# result = pd.concat(result, axis=0)

print(result)

result.to_sql(name='test6', con=engine, if_exists='append',index=False) #,dtype=dtypedict)  # 写入


# parameters={'album_name': '莎话', 'language': 0, 'lyric': '分手说爱你 - 阿悄/王麟\\n词：阿悄\\n曲：阿悄\\n编曲：夏侯哲\\n录音：谭炜星\\n缩混：夏侯哲\\n分手说爱你 谁也别去回忆\\n再委屈 都跟你 没关系\\n分手说爱你 谁也别提分离\\n都怪我 太爱你 太恨你\\n那些甜 那些蜜 这遥远的距离\\n时间推移 我们回不到过去\\n你爱 ... (290 characters truncated) ...  我想不通\\n你总是爱爱爱爱 爱不够\\n请你别说 你一直会失落\\n分手说爱你 谁也别去回忆\\n再委屈 都跟你 没关系\\n分手说爱你 谁也别提分离\\n都怪我 太爱你 太恨你\\n分手说爱你 谁也别去回忆\\n再委屈 都跟你 没关系\\n分手说爱你 谁也别提分离\\n都怪我 太爱你 太恨你', 'singer_id': [22855, 12242], 'singer_mid': ['0040Eq913AwwEZ', '001f0CIZ04Sh6X'], 'singer_name': ['阿悄', '王麟'], 'song_id': 5099859, 'song_mid': '000Ewl3s2p27I8', 'song_name': '分手说爱你', 'song_time_public': '2013-12-24', 'song_type': 0, 'song_url': 'https://y.qq.com/n/yqq/song/000Ewl3s2p27I8.html', 'subtitle': ''}, {'album_name': '空', 'language': 0, 'lyric': '当卖火柴的小女孩 遇上 放烟火的小男孩 - 阿悄/小贱（谭冰尧）\\n女：雪花纷飞\\n冰冷的美\\n花儿枯萎\\n我浇灌热泪\\n好想安睡\\n谁可以哄我入睡\\n借我一张棉被\\n男：我走过很长的路\\n攀爬过很高的树\\n一生寻觅的宝物\\n隐藏在你的泪珠\\n女：可不可以抱住我\\n答应我 ... (182 characters truncated) ... 男：你不要哭\\n女：好的\\n男：我喜欢你笑\\n女：好的\\n我会每天笑着等你回家做饭给你\\n你爱吃什么菜\\n男：都可以\\n女：你爱喝什么汤\\n男：都可以\\n女：Oh宝贝 没有材料\\n你自己去买\\n男：噢 可以可以\\n女：Oh宝贝 开玩笑的\\n我陪你去买\\n男：嗯 很好很好', 'singer_id': [22855, 16292], 'singer_mid': ['0040Eq913AwwEZ', '001ZRG9K1UUgk9'], 'singer_name': ['阿悄', '小贱（谭冰尧）'], 'song_id': 1035318, 'song_mid': '0006gRFZ07hxma', 'song_name': '当卖火柴的小女孩 遇上 放烟火的小男孩', 'song_time_public': '1990-01-01', 'song_type': 0, 'song_url': 'https://y.qq.com/n/yqq/song/0006gRFZ07hxma.html', 'subtitle': ''}, {'album_name': '我真的一点都不孤单', 'language': 0, 'lyric': '我真的一点都不孤单 - 阿悄\\n词：阿悄\\n曲：阿悄\\n编曲：谭炜星\\n混音：符式龙\\n离去的时候 你不说话\\n冷冷看着我 痛哭的脸庞\\n做敌人能让彼此 好受些吧\\n过去的嬉笑 有多灿烂\\n现在的煎熬 有多艰难\\n你不必紧张 反正我也无妨\\n也许\\n爱未必都是快乐\\n恨未 ... (105 characters truncated) ... 的泪水\\n流进眼眶\\n我其实也没有想念那些时光\\n只是怀念 你孩子气时的模样\\n你说爱我的那个夜晚 和今天好像\\n还有什么好说\\n这也不是我资格\\n我只想要能够\\n给你最大的自由\\n我发誓我真的一点都不孤单\\n天气好冷 我只想一个人回家\\n好让哽咽在喉咙间的泪水\\n流出眼眶', 'singer_id': [22855], 'singer_mid': ['0040Eq913AwwEZ'], 'singer_name': ['阿悄'], 'song_id': 108750906, 'song_mid': '000XewvH0aoR7s', 'song_name': '我真的一点都不孤单', 'song_time_public': '2016-09-27', 'song_type': 0, 'song_url': 'https://y.qq.com/n/yqq/song/000XewvH0aoR7s.html', 'subtitle': ''}, {'album_name': '亲爱的理由', 'language': 0, 'lyric': '我唱着歌会想你 - 阿悄\\n词：阿悄\\n曲：阿悄\\n你的誓言我不相信\\n但也不是我不可惜\\n事到如今虽然笑着\\n眼泪流得很无力\\n开始总是很美丽\\n所以显得遥不可及\\n粹不及防我的心情\\n你留在哪我看不清\\n谁制造失落\\n散在世界角落\\n怎么闪躲\\n也眼眶泛红\\n星星 ... (284 characters truncated) ... \\n你住在我心底\\n却从此走出我的生命里\\n我唱着歌会想你还是那个你\\n像玻璃的回忆\\n刺进我的生命\\n我唱着歌会想你独守到天明\\n你住在我心底\\n却从此走出我的生命里\\n我唱着歌会想你还是那个你\\n像玻璃的回忆\\n刺进我的生命\\n我唱着歌会想你独守到天明\\n你住在我心底', 'singer_id': [22855], 'singer_mid': ['0040Eq913AwwEZ'], 'singer_name': ['阿悄'], 'song_id': 4918695, 'song_mid': '004UIVe31cvcWn', 'song_name': '我唱着歌会想你', 'song_time_public': '2013-06-25', 'song_type': 0, 'song_url': 'https://y.qq.com/n/yqq/song/004UIVe31cvcWn.html', 'subtitle': ''}, {'album_name': '空', 'language': 0, 'lyric': '遇 - 阿悄\\n词：Vannessa\\n曲：Vannessa\\n都怪雨下得那么急\\n都怪没有地方躲雨\\n才会一头撞进了你的怀里\\n跌进你深深的眼里\\n都怪梦境太过迷离\\n都怪你身影太清晰\\n总是听见雨水耳边滴答滴\\n忘不了你温柔表情\\n自从遇见你的那天起\\n我的心就不再属于 ... (169 characters truncated) ... 形\\n猜不透这是什么道理\\n怎会想你想到昏天又暗地\\n难道这就是他们说的爱情\\n已悄悄闯进心里\\n自从遇见你的那天起\\n我的心就不再属于我自己\\n不管上天下地都看见你\\n想念如影随形\\n猜不透这是什么道理\\n怎会想你想到昏天又暗地\\n难道这就是他们说的爱情\\n已悄悄闯进心里', 'singer_id': [22855], 'singer_mid': ['0040Eq913AwwEZ'], 'singer_name': ['阿悄'], 'song_id': 206334928, 'song_mid': '004fosVU3jQVlN', 'song_name': '遇', 'song_time_public': '1990-01-01', 'song_type': 0, 'song_url': 'https://y.qq.com/n/yqq/song/004fosVU3jQVlN.html', 'subtitle': ''}