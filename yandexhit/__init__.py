#!/usr/bin/env python
#coding:utf8

#!/usr/bin/env python
#coding:utf8
import urllib
import requests
import random


class YaHit(object):

    URL = 'https://mc.yandex.ru/watch/'

    def __init__(self, counter):
        self.counter = counter

    def hit(self, pageUrl='', pageRef='', **args):
        data = {}
        ip = args.pop('ip', '')

        def setPar(name, val):
            if val:
                data[name] = val

        setPar('page-url', pageUrl)
        setPar('page-ref', pageRef)
        data['browser-info'] = 'en:utf-8'
        url_values = urllib.urlencode(args)
        getQuery = '%s/1?rn=%s&wmode=2&' % (self.counter, random.randint(0, 100000))
        getQuery += url_values
        URL = self.URL+getQuery
        #print URL
        headers = {}
        if ip:
            headers['X-Real-IP'] = ip

        r = requests.post(self.URL+getQuery, data, headers=headers)
        #print r.content

