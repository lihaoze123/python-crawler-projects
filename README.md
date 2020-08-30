## 前言 

这个仓库存放我暑假学习Python完成的一些爬虫项目，因为明天开学所以上传到Github上面开源，不小心瞅见这个项目的小哥哥小姐姐们记得给个star再走哦(爱心)



## 有哪些

目前为止我完成的Python项目有:

| 文件名 | 功能 | 介绍 |
|:---:|:--:|:--:|
|Bilibili_rank|查询bilibili日排行榜|只需调用**bilibili.py**中的bilibili_rank函数(传入number参数)|
|AI_talk|和ai智能机器人聊天|调用**[小i机器人](http://i.xiaoi.com/)**API,能实现和<del>智能</del>智障聊天的功能|
|Suo|查询奇奇怪怪的缩写|原项目:**[nbnhhsh](https://github.com/itorr/nbnhhsh)**,本项目调用网页版API,调用**suo**函数,传入字符串,如```"xz"```,会返回类似于**肖战**的字符串|
|Geng|查询梗|调用**[小鸡词典](https://jikipedia.com/)**API|



## 如何使用

**首先**,clone此项目,在项目文件夹中打开终端,<br>输入```pip install -r reqrequirements.txt ```<br>**然后**,调用项目文件中的函数(以Bilibili_rank为例)

```python
from bilibili_rank import bilibili_rank
print(bilibili_rank(3))
```

此行为会打印类似于

>  排名：1  播放量：271.1万  弹幕数：1.1万 
> 标题：国内外挂开发者大战腾讯程序员   
> 链接：https://www.bilibili.com/video/BV1t54y1v76b 
> up名：国电武术馆馆长  ta的空间：https://space.bilibili.com/235630215 
>
> 排名：2  播放量：86.8万  弹幕数：3299 
> 标题：[硬核科普]教你五秒快速睡眠!   
> 链接：https://www.bilibili.com/video/BV1LZ4y1T752 
> up名：亮生活-BrightSide  ta的空间：https://space.bilibili.com/668813734 
>
> 排名：3  播放量：127.3万  弹幕数：8223 
> 标题：【罗翔】做自己，要先明白自己是谁   
> 链接：https://www.bilibili.com/video/BV1t54y1v7hF 
> up名：果麦麦榨知机  ta的空间：https://space.bilibili.com/538013441

的字符串。



其他项目文件使用方法类似



##  小提示

给一颗star会让我产出更多优质项目哦