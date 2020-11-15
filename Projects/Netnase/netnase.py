import re
import logging
import requests
from tqdm import tqdm


def downloader(id, filename):
    headers = { 'User-agent':
            'Mozilla/5.0 (X11; Linux x86_64; rv:57.0)Gecko/20100101 Firefox/57.0',
            'Host':'music.163.com',
            'Referer':'https://music.163.com'}
    url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(id)
    logging.info("得到url:" + url)
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response = requests.get(response.headers["location"], stream=True)
        logging.debug(response.headers)
        logging.info(
            "文件大小:" + str(int(response.headers["Content-Length"]) / 1024 / 1024) + "MB")
        logging.info("开始写入")
        logging.info("写入文件:" + filename + ".mp3")
        with open("./{}.mp3".format(filename), "wb") as f:
            for i in tqdm(response.iter_content()):
                f.write(i)
    except requests.exceptions.SSLError:
        logging.debug("请确保id正确")
    else:
        logging.info("写入成功！")


def get_id(url):
    logging.info("输入的内容:" + url)
    try:
        int(url)
    except ValueError:
        if "music.163.com/#/song?id=" in url:
            for i in re.findall(re.compile(r'[0-9]*'), url):
                if i and i != "163":
                    logging.info("获取到的id(从链接获取):" + i)
                    return i
    else:
        logging.info("已经输入的id:" + url)
        return url


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    downloader(get_id(input("请输入链接\n")), input("请输入文件名\n"))
