import requests
import json

__author__ == "Chumeng"

def suo(word):
    url = "https://lab.magiconch.com/api/nbnhhsh/guess"
    data = {"text": word}

    r = requests.post(url, data=data).text
    sx = json.loads(r)[0]["name"]
    try:
        trans = json.loads(r)[0]["trans"]
        trans = " | ".join(trans[0:])
        trans = "搜查到的结果: \n{}".format(trans)
        return trans
    except KeyError:
        return "网络上没有找到此缩写"

if __name__ == "__main__":
   print(suo(input("请输入要查询的缩写\n")))
