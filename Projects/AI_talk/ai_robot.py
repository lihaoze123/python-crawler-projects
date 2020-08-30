import requests, re
from urllib.parse import quote

__author__ = "Chumeng"

def ai_robot(sentence):
    sessionid = "test"
    nonce = "test"
    # 爬虫
    data = '{"sessionId":"ca22c6b008d941849e7f3444fee66339","robotId":"webbot","userId":"481ee89814b44d13b837eba247f3f1c5","body":{"content":"%s"},"type":"txt"}' % \
            sentence
    url = 'http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%s&ts=1596985917633' % quote(data)

    header = {
        'Cookie': "XISESSIONID=%s;nonce=%s" % (sessionid, nonce),
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 84.0.4147.105Safari / 537.36Edg / 84.0.522.52'
    }

    r = requests.get(url, headers=header).text
    # 匹配
    compile = re.compile(r'"content":".*?"')
    result = re.findall(compile, r)[1]
    content_compile = re.compile(r'".*?"')
    result = re.findall(content_compile, result)[1]
    content = re.sub(r'"', "", result)
    content = re.sub(r"\\r\\n", "", content)

    return content

if __name__ == "__main__":
    print(ai_robot(input("请输入句子\n")))
