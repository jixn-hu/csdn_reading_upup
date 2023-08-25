# -*- coding: utf-8 -*-
# @Time    : 2023/8/25 9:57
# @Author  : XXX
# @Site    : 
# @File    : main.py
# @Software: PyCharm 
# @Comment :
import random
import re
import time
from pathlib import Path
from loguru import logger
import requests
import yaml

f = Path('config.yaml').read_text(encoding='utf-8')
config = yaml.safe_load(f)
proxys = random.sample(config["proxy"],len(config["proxy"]))
csdnRRS = config["csdnRRS"]["url"]
logger.add("logs/{time:YYYY-MM-DD}.log",rotation='00:00',retention='7 days')

def run():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(csdnRRS, headers=headers)

    print(response)
    print(response.text)
    if response.status_code==200 and r'xml' in response.text:
        logger.info("正常")
        links = re.findall(r'title>\s*<link>([^<>]*?)</link>',response.text)
        logger.info(links)
        for proxy in proxys:
            links = random.sample(links, len(links)-5)
            for link in links:
                print(proxy,link)
                go_link(proxy,link)

def go_link(proxy,url='https://blog.csdn.net/qq_37462361/article/details/132275183'):
    time.sleep(random.random()*10)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    proxies = {
        "http": f'http://{proxy}',
        "https": f'http://{proxy}'
    }
    response = requests.get(url, headers=headers,proxies=proxies)
    print(response)
    time.sleep(random.random() * 5)

if __name__=='__main__':
    run()