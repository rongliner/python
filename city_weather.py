#!/usr/bin/python
# coding:utf-8
# auther: rongliner
"""
输入城市名称，查对应的天气
"""
from city import city   # 通过city_weather_code.py 获取 city.py
import urllib2
import json

cityname = raw_input("请输入要天气的城市名称？\n")
citycode = city.get(cityname)
if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        content = response.read()
        # print content
        """
        {"weatherinfo":{
        "city":"赣州",
        "cityid":"101240701",
        "temp1":"8℃",
        "temp2":"24℃",
        "weather":"晴",
        "img1":"n0.gif",
        "img2":"d0.gif",
        "ptime":"18:00"}}
        """
        data = json.loads(content)
        result = data['weatherinfo']
        str_temp = ('%s\n%s ~ %s') % (result['weather'], result['temp1'], result['temp2'])  # 温度
        print str_temp
    except:
        print "查询失败"
else:
    print "没有找到该城市" 



