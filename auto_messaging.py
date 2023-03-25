# -*- coding: utf-8 -*-
# created by Morty Liu on 2022/7/6

import pyperclip
import requests
import datetime
from utils import *
import time
import os

city_id = '101080201'
city_id = '101280101'


def get_news():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def get_sentence(api):
    santence = requests.get(api)
    return santence.json()


def open_app(app_dir):
    os.startfile(app_dir)


def get_weather():
    name = 'http://t.weather.sojson.com/api/weather/city/' + city_id
    g2 = get_sentence(name)
    times = g2['cityInfo']

    city = times['city']
    parent = times['parent']

    time1 = g2['data']

    shidu = time1['shidu']
    pm25 = time1['pm25']
    quality = time1['quality']

    time2 = time1.get('forecast', '不存在该键')
    time2 = time2[0]

    high = time2['high']
    low = time2['low']
    fx = time2['fx']
    fl = time2['fl']
    type = time2['type']
    notice = time2['notice']

    t = datetime.datetime.now()
    print(f'{t.hour}:{t.minute}:{t.second}')

    string = f'所在省份：{parent}\n' \
             f'所在城市：{city}\n' \
             f'今日温度：{low[3:-1]}-{high[3:-1]}℃\n' \
             f'风向：{fx}\n' \
             f'风力：{fl}\n' \
             f'湿度：{shidu}\n' \
             f'PM2.5：{pm25}\n' \
             f'空气质量：{quality}\n' \
             f'天气：{type}-{notice}\n'

    return string


def get_message(message):
    init_message = "messages you want to send!\n"
    if not message:
        message = init_message
    daily_eng, daily_ch = get_news()
    weather = get_weather()
    string = message + weather + '每日一句：' + daily_eng + '\n' + daily_ch + '\n'
    print(string)
    return string


def search_object(name='文件传输助手'):
    ctrl_f()
    pyperclip.copy(name)
    ctrl_v()
    enter()


def type_message(message=None):
    string = get_message(message)
    pyperclip.copy(string)
    ctrl_v()
    enter()


def send_message(message=None):
    if not message:
        return

    pyperclip.copy(message)
    ctrl_v()
    time.sleep(1)
    enter()


while True:
    time_now = time.strftime("%H:%M", time.localtime())  # 获取当前时间
    print(time_now)
    if time_now == "07:00":  # 此处为消息发送的时间

        app_dir = r'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe'  # 此处为微信的绝对路径
        open_app(app_dir)
        time.sleep(1)  # 电脑反应需要时间，使程序暂停一段时间来等待电脑反应，单位是秒

        search_object('wechat name')
        # search_object()
        type_message()
        send_message("路上注意安全！到了记得发消息哦！")

    time.sleep(59)
