import logging
from time import sleep
import time
import datetime
import requests
import os
import json

SCKEYS = {  # 微信推送api，到http://sct.ftqq.com/ 免费申请，不需要请留空
    "jyc": "SCT75973TaWGs5q1KAYUqptNTJgAmPsOi",
    "yrz": "SCT76151TWwe3EuGQ1WFwPBjYc4nx3Fq1",
    "wzy": "SCT74683TvDNNjkYEt9K9tsDWI7NtuyKX",
    "jhy": "SCT76061T9TPuWaBXHo6irdOssUEY34qT"
    }
duty_order = ['yrz', 'jyc', 'jhy', 'wzy']

with open("record.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)

on_duty = duty_order[int(load_dict['duty_times'])%len(duty_order)]
print(on_duty)

load_dict['duty_times'] = load_dict['duty_times'] + 1
with open("record.json","w") as dump_f:
    json.dump(load_dict,dump_f)


def remind():
    send_message("值日提醒", SCKEYS[on_duty], "hello, 今天你值日哦 ^_^")
    logger.info("done")



def main():
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

