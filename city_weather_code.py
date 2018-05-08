#!/usr/bin/python
# coding:utf-8
# auther: rongliner
import urllib2
"""
获取城市天气代码（执行的时候比较慢,需要优化）
"""


def get_province(url):
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        contents = response.read()
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
        if lines.isdigit():
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
    for line in lines.split(','):
        m = line.replace('|',',')
        n =  m.split(',')
        if len(n)>=2:
            with open(filepath,'a+') as f:
                f.write(n[1])
                f.write(':')
                f.write(str('101'+n[0])+'\n')



if __name__ == "__main__":
    filepath = 't.txt'
    main(filepath)
