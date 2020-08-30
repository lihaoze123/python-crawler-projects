from lxml import etree
import requests

__author__ == "Chumeng"

def bilibili_rank(number):
    #爬虫
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49'
    }
    url = 'https://www.bilibili.com/ranking'
    res = requests.get(url, headers=header).text

    #提取
    soup = etree.HTML(res)

    ranks = soup.xpath(
        '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[1]/text()')
    links = soup.xpath(
        '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/a/@href'
    )
    titles = soup.xpath(
        '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/a/text()'
    )
    up_names = soup.xpath(
        '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[1]/a/span/text()'
    )
    up_spaces = soup.xpath(
        '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[1]/a/@href'
    )
    views = soup.xpath(
        '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[1]/span[1]/text()'
    )
    danmus = soup.xpath(
        '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[1]/span[2]/text()'
    )

    result = []
    for i in range(0, number):
        result.append("排名：%s   播放量：%s   弹幕数：%s"%(ranks[i], views[i], danmus[i]) + "\n标题：%s    \n链接：%s"%(titles[i], links[i]) + "\nup名：%s"%up_names[i] + "   ta的空间：https:%s\n"%up_spaces[i])

    post = "\n".join(result)

    return post

if __name__ == "__main__":
    print(bilibili_rank(3))
