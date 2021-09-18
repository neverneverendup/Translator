#-*- coding:utf-8 -*-

import time
import hashlib
import requests
import random

class Youdao():

    def __init__(self):

        self.lan_dict={
            '中文':'zh-CHS',
            '英文': 'en',
            '俄文': 'ru',
            '法文': 'fr',
            '日文': 'ja',
            '韩文': 'ko'
            }
        self.s = requests.Session()
        self.s.keep_alive = False
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            'Referer': 'http://fanyi.youdao.com/',
            'contentType': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-352392290@116.136.20.84; P_INFO=a121bc; OUTFOX_SEARCH_USER_ID_NCOO=710017829.1902944; JSESSIONID=aaaDa3sqezCDY-snjj91w; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=' + str(
                int(time.time() * 1000)),
        }
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    def translate(self,from_lan,to_lan,text):
        self.headers['Content-Length'] = str(233 + len(text))
        ts = str(int(time.time() * 1000))
        salf = ts + str(random.randint(0, 9))
        n = 'fanyideskweb' + text + salf + "Tbh5E8=q6U3EXe+&L[4c@"
        self.m = hashlib.md5()
        self.m.update(n.encode('utf-8'))
        sign = self.m.hexdigest()
        data = {
            'i': text,
            'from': from_lan,
            'to': to_lan,
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salf,
            'sign': sign,
            'ts': ts,
            'bv': '53539dde41bde18f4a71bb075fcf2e66',
            'doctype': 'json',
            'version': "2.1",
            'keyfrom': "fanyi.web",
            'action': "FY_BY_REALTlME"
        }
        try:
            result = self.s.post(self.url, headers=self.headers, data=data, timeout=5).json()
            print(result)
            if result != None:
                ans = result['translateResult'][0][0]['tgt']
                return ans
            else:
                return None
        except Exception as e:
            return None

if __name__ == '__main__':

        yd = Youdao()
        text = '你好'
        print(yd.translate('zh-CHS','en',text))

