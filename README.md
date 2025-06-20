<h1 style="font-size: 2em;">😀 同步网易云到 Notion</h1>
---

<img width="324" alt="微信图片_20250620101556" src="https://github.com/user-attachments/assets/a574c733-e505-41a8-a210-ec7444dfd7a5" />
![wechatQR](https://github.com/user-attachments/assets/9a5879fa-7719-40de-af30-0f2433bc679c)


---
点个关注喵😸 永雏塔菲谢谢你喵😽


# 📝 效果展示



https://www.chalice.lol/essay/1f93a17d-9c21-8169-baa5-c65aff1c6b6c
<br>
<br>
https://garnet-scarer-ec7.notion.site/2033a17d9c2180a9a50bf2226f9c42ef?v=2033a17d9c2181f9aeb1000ccd927682&pvs=74
![image](https://github.com/user-attachments/assets/8524165e-848d-4600-959f-9ace25162658)


## 第一步（不方便演示，dddd）

请你在github上自行搜索cookie获取个人帐号json文件的方式

大概能用的方式有：

GET /user/detail?uid=xxxx 获取用户基本信息

GET /user/record?uid=xxxx&type=1 获取所有时间听歌记录（包含每首歌听了多少次，总听歌时长）

GET /user/record?uid=xxxx&type=0 一周

GET /user/playlist?uid=xxxx 获取用户的歌单

GET /playlist/detail?id=xxxx 获取歌单详情（歌曲列表）

得到对应的json文件


## 第二步（json转csv导入notion）

仓库中有两个.py文件供参考，得到带表头的csv文件

![image](https://github.com/user-attachments/assets/ee21f561-9399-4d95-a810-97d9f6e24ada)

你可以复制我的模板，也可以新建一个画廊

![image](https://github.com/user-attachments/assets/2551475e-ba73-441a-8f7d-50e6469089a3)

![image](https://github.com/user-attachments/assets/03961c34-c466-493b-82cf-b5a114b80890)

右上角导入——csv（UTF-8,否则会乱码）

![image](https://github.com/user-attachments/assets/492f5df5-b075-435d-8681-d2b1a992f5bb)




## 第三步（调整和展示）

![image](https://github.com/user-attachments/assets/57b8cf18-d2c3-4013-81b3-c623a4403509)


这时候你会发现不显示封面，需要点击“属性”——“封面”，修改为“媒体和文件”

并在“布局”——“卡片预览”替换成“封面”这个属性。

![image](https://github.com/user-attachments/assets/49d703da-49ed-47a4-99e7-ea652c443cf2)


 通过 显示/隐藏属性、自定义属性，来调整你想展示的内容

![image](https://github.com/user-attachments/assets/a2507fe3-a3b2-409f-9944-0281080e23e8)


notion无法展示属性名，只会展示属性的内容，这时候你可以新建属性——函数

> "播放次数 " + format(prop("播放次数"))
> 

来显示“播放次数：”

最终结果。

![image](https://github.com/user-attachments/assets/8524165e-848d-4600-959f-9ace25162658)

# 🤗 总结归纳

可以通过复制notion数据库页面的分享链接粘贴到其他数据库页面，会自动引用（不要用复制粘贴）

![image](https://github.com/user-attachments/assets/06eb1b1d-7e6f-4d9d-90bb-2bf8ff09ba46)

<aside>
💡 有关Notion安装或者使用上的问题，欢迎您在底部评论区留言，一起交流~

</aside>
