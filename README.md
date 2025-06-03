<aside>
😀 赛博手账制作碎片

</aside>

# 📝 效果展示

![image.png](attachment:ed14fb1b-518d-44b8-9af6-dfc6897acb24:image.png)

## 第一步（不方便演示，dddd）

请你在github上自行搜索获取个人帐号json文件的方式

大概能用的方式有：

GET /user/detail?uid=xxxx 获取用户基本信息

GET /user/record?uid=xxxx&type=1 获取所有时间听歌记录（包含每首歌听了多少次，总听歌时长）

GET /user/record?uid=xxxx&type=0 一周

GET /user/playlist?uid=xxxx 获取用户的歌单

GET /playlist/detail?id=xxxx 获取歌单详情（歌曲列表）

得到对应的json文件

## 第二步（json转csv导入notion）

仓库中有两个.py文件供参考，得到带表头的csv文件

![image.png](attachment:f588edc3-c720-44ee-b4cb-abc1044c9c7a:image.png)

你可以复制我的模板，也可以新建一个画廊

[https://www.notion.so/2023a17d9c21815a8f78cff14dd7e9f6?v=2023a17d9c2181a9aabc000ce8255902&source=copy_link](https://www.notion.so/2023a17d9c21815a8f78cff14dd7e9f6?pvs=21)

![image.png](attachment:822aab04-3b78-40fc-aa87-278d1741e25f:image.png)

![image.png](attachment:95fbb661-da09-4fa7-9705-e2ac93b6c37b:image.png)

右上角导入——csv（UTF-8,否则会乱码）

![image.png](attachment:f584b402-7883-46e0-a201-ec1c28b8fa57:image.png)

## 第三步（调整和展示）

![image.png](attachment:dde677ac-fbab-49df-828e-51e48b0a450c:image.png)

这时候你会发现不现实封面，点击“属性”——“封面”，修改为“媒体和文件”

并在“布局”——“卡片预览”替换成封面这个属性。

![image.png](attachment:cffa2977-b07a-4e1a-97a6-fc13bc321a07:image.png)

 通过 显示/隐藏属性、自定义属性，来调整你想展示的内容

![image.png](attachment:070da14a-1760-4124-b265-de8cc83fec87:image.png)

notion无法展示属性名，只会展示属性的内容，这时候你可以新建属性——函数

> "播放次数 " + format(prop("播放次数"))
> 

来显示“播放次数：”

最终结果。

![image.png](attachment:ed14fb1b-518d-44b8-9af6-dfc6897acb24:image.png)

# 🤗 总结归纳

可以通过复制notion数据库页面的分享链接粘贴到其他数据库页面，会自动引用（不要用复制粘贴）

![image.png](attachment:31992585-9c75-4de3-b1b0-d5f8403a4074:image.png)

<aside>
💡 有关Notion安装或者使用上的问题，欢迎您在底部评论区留言，一起交流~

</aside>
