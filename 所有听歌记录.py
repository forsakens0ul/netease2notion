import json
import csv
from datetime import datetime

# 读取JSON文件
with open('d:/2/netease/所有时间听歌记录.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 准备CSV文件
with open('netease_songs.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    
    # 写入表头
    writer.writerow([
        '歌曲名', '歌手', '专辑', '封面', 
        '播放次数', '播放得分', '发行时间', 
        '时长', '是否VIP', '是否已购买', 'MV', '音质'
    ])
    
    # 处理每条歌曲数据
    for item in data['allData']:
        song = item['song']
        
        # 处理歌手名（合并多个歌手）
        artists = [ar['name'] for ar in song['ar']]
        artist_names = ' / '.join(artists)
        
        # 处理时长（ms转分钟:秒）
        duration_ms = song['dt']
        minutes = duration_ms // 60000
        seconds = (duration_ms % 60000) // 1000
        duration = f"{minutes}:{seconds:02d}"
        
        # 处理发布时间（时间戳转日期）
        publish_time = datetime.fromtimestamp(song['publishTime']/1000).strftime('%Y-%m-%d')
        
        # 处理音质
        sq_info = song.get('sq', {}) or {}
        sq_br = sq_info.get('br', 0)
        if sq_br >= 999000:
            quality = f"无损（{sq_br//1000}kbps）"
        elif sq_br >= 320000:
            quality = f"高品质（{sq_br//1000}kbps）"
        else:
            quality = f"标准（{sq_br//1000}kbps）"
        
        # 处理MV链接
        mv_id = song.get('mv', 0)
        mv_url = f"https://music.163.com/mv?id={mv_id}" if mv_id else ""
        
        # 写入一行数据
        writer.writerow([
            song['name'],                     # 歌曲名
            artist_names,                     # 歌手
            song['al']['name'],               # 专辑
            song['al']['picUrl'],             # 封面
            item['playCount'],                # 播放次数
            item['score'],                    # 播放得分
            publish_time,                     # 发行时间
            duration,                         # 时长
            '是' if song['fee'] > 0 else '否', # 是否VIP
            '是' if song['privilege']['payed'] > 0 else '否', # 是否已购买
            mv_url,                          # MV链接
            quality                           # 音质
        ])

print("CSV文件已生成：netease_songs.csv")
