#!/usr/bin/python
# coding:utf-8
# auther: rongliner
import urllib2
"""
获取城市天气代码（执行的时候比较慢,需要优化）
httplib.BadStatusLine: '' -- 出现这个报错一般都是没有User-Agent
"""


def get_province(url):
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        contents = response.read()    # 获取网页内容
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print e.code
        if hasattr(e, 'reason'):
            print e.reason
    return contents

def get_list(contents):
    lists = ''
    contents = contents.replace('|',',')
    for lines in contents.split(','):
        if lines.isdigit():     # 判断是否是数字
            url = 'http://m.weather.com.cn/data3/city' + lines + '.xml'
            line = get_province(url)
            lists += line
            lists +=','
    return lists

def main(filepath=None):
    url = 'http://m.weather.com.cn/data3/city.xml'
    contents = get_province(url)
    lists =  get_list(contents)
    lines = get_list(lists)
    city = {}
    for line in lines.split(','):
        m = line.replace('|',',')
        n =  m.split(',')
        if len(n)>=2:
            city[n[1]] = str('101'+n[0])
    with open(filepath,'a+') as f:
        f.write('#!/usr/bin/python\n#coding:utf-8\n\n')
        f.write('city='+str(city))
        f.write('\n')



if __name__ == "__main__":
    filepath = 'citys.py'
    main(filepath)
