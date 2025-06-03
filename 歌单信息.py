import json
import csv
from datetime import datetime

def extract_song_info(song):
    try:
        # 处理歌手名（合并多个歌手）
        artists = [ar.get('name', '未知歌手') for ar in song.get('ar', [])]
        artist_names = ' / '.join(artists) if artists else "未知艺术家"
        
        # 处理时长（ms转分钟:秒）
        duration_ms = song.get('dt', 0)
        minutes = duration_ms // 60000
        seconds = (duration_ms % 60000) // 1000
        duration = f"{minutes}:{seconds:02d}"
        
        # 处理发布时间（时间戳转日期）
        publish_time = "未知日期"
        if song.get('publishTime'):
            try:
                publish_time = datetime.fromtimestamp(song['publishTime']/1000).strftime('%Y-%m-%d')
            except:
                pass
                
        # 处理音质
        sq_br = song.get('sq', {}).get('br', 0)
        bitrate = f"{sq_br//1000} kbps" if sq_br > 0 else "N/A"
        
        # 处理MV链接
        mv_id = song.get('mv', 0)
        mv_url = f"https://music.163.com/mv?id={mv_id}" if mv_id else ""
        
        return {
            'Song': song.get('name', '未知歌曲'),
            'Artist': artist_names,
            'Album': song.get('al', {}).get('name', '未知专辑'),
            'Cover': song.get('al', {}).get('picUrl', ''),
            'Duration': duration,
            'Bitrate': bitrate,
            'Popularity': song.get('pop', 0),
            'MV Link': mv_url,
            'Paid': '是' if song.get('fee', 0) > 0 else '否',
            'Release Date': publish_time
        }
    except Exception as e:
        print(f"处理歌曲时出错: {str(e)}")
        return None

def main():
    try:
        with open('d:/2/netease/获取歌单详情.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not data.get('playlist', {}).get('tracks'):
            raise ValueError("JSON文件缺少必要的playlist或tracks字段")
            
        # 分批处理设置
        batch_size = 500  # 每批处理500条记录
        total = len(data['playlist']['tracks'])
        
        with open('netease_playlist_songs.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = [
                'Song', 'Artist', 'Album', 'Cover', 
                'Duration', 'Bitrate', 'Popularity', 
                'MV Link', 'Paid', 'Release Date'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            # 分批处理数据
            for i in range(0, total, batch_size):
                batch = data['playlist']['tracks'][i:i+batch_size]
                for song in batch:
                    song_info = extract_song_info(song)
                    if song_info:
                        writer.writerow(song_info)
                
                print(f"已处理 {min(i+batch_size, total)}/{total} 条记录")
                csvfile.flush()  # 确保数据写入磁盘

        print(f"CSV文件已成功生成，共处理 {total} 条记录")
        
    except Exception as e:
        print(f"发生错误：{str(e)}")

if __name__ == '__main__':
    main()