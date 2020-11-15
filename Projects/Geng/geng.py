import requests
from lxml import etree, html

__author__ = "Chumeng"

def geng(ask):
    #爬虫
    url = 'https://jikipedia.com/search?phrase=' + ask
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49',
        'Cookie':
        'XID=32e14b0c-938c-4f9e-8b30-69876212d76a; Hm_lvt_63a8941b9af78a70fb9a9951990bbcbd=1597035491; Hm_lpvt_63a8941b9af78a70fb9a9951990bbcbd=1597035491; __gads=ID=0616f4f988904760:T=1597035493:S=ALNI_MaEX8dm7pN0jueU7yFvuGb6tNN7Yw'

    }

    res = requests.get(url, headers=headers).text
    html = etree.HTML(res)

    #提取

    links = ''.join(
        html.xpath('//*[@id="search"]/div/div[2]/div[1]/div/a/@href'))
    writers = ''.join(
        html.xpath(
            '//*[@id="search"]/div/div[2]/div[1]/div/div[2]/div[1]/a/text()'))
    titles = ''.join(
        html.xpath('//*[@id="search"]/div/div[2]/div[1]/div/a/@title'))
    divs = ''.join(
        html.xpath(
            '//*[@id="search"]/div/div[2]/div[1]/div/a/div[1]/div[2]/div/span/span/text()'
        ))

    total = {
        'link': 'https://jikipedia.com' + links,
        'writer': writers,
        'title': titles,
        'div': divs
    }

    exam = html.xpath(
            '//*[@id="search"]/div/div[2]/div[1]/div/a/div[1]/div[2]/div/span/span/text()'
        )

    if len(exam) > 0:
        post = "原回答链接：%s\n" % total['link'] + "\n标题：%s\n" % total['title'] + "正文：\n%s" % total['div']
    else: post = "网络上没有此问题的答案"

    return post

if __name__ == "__main__":
    print(geng("nmsl"))

