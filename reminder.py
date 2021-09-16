import logging
from time import sleep
import time
import datetime
import requests
import os

SCKEYS = {  # 微信推送api，到http://sct.ftqq.com/ 免费申请，不需要请留空
    "jyc": "SCT75973TaWGs5q1KAYUqptNTJgAmPsOi",
    "yrz": "",
    "wzy": "",
    "jhy": ""
    }
on_duty = os.getenv('ON_DUTY')

def remind():
    send_message("值日提醒", SCKEYS[on_duty], "hello, 今天你值日哦 ^_^")
    logger.info("done")



def main():
    logger.info("正在进行验证...")
    send_message("hello world")
    remind()


def send_message(msg, to_whom = '', msgcnt = ''):
    if to_whom == "":
        return
    payload = {'title': msg, 'desp': msgcnt}
    requests.get(f"https://sctapi.ftqq.com/{to_whom}.send", params=payload)


if __name__ == "__main__":
    log_file = "log.log"
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    logger = logging.getLogger("main")
    fh = logging.FileHandler(log_file, mode='w')
    fh.setFormatter(formatter)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)
    main()

