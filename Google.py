# -*- coding:utf-8 -*-

import urllib
import urllib.request
import urllib.parse
import requests
import execjs


class Google():
    def __init__(self):

        self.lan_dict = {
            '中文': 'zh-CN',
            '英文': 'en',
            '俄文': 'ru',
            '法文': 'fr',
            '日文': 'ja',
            '韩文': 'ko'
        }

        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
        self.url = 'http://translate.google.cn/translate_a/single'
        self.session = requests.Session()
        self.session.keep_alive = False

    def getTk(self, text):
        return self.get_ctx().call("TL", text)

    def get_ctx(self):
        ctx = execjs.compile(""" 
        function TL(a) { 
        var k = ""; 
        var b = 406644; 
        var b1 = 3293161072; 
        var jd = "."; 
        var $b = "+-a^+6"; 
        var Zb = "+-3^+b+-f"; 
        for (var e = [], f = 0, g = 0; g < a.length; g++) { 
            var m = a.charCodeAt(g); 
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
            e[f++] = m >> 18 | 240, 
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
            e[f++] = m >> 6 & 63 | 128), 
            e[f++] = m & 63 | 128) 
        } 
        a = b; 
        for (f = 0; f < e.length; f++) a += e[f], 
        a = RL(a, $b); 
        a = RL(a, Zb); 
        a ^= b1 || 0; 
        0 > a && (a = (a & 2147483647) + 2147483648); 
        a %= 1E6; 
        return a.toString() + jd + (a ^ b) 
    }; 

    function RL(a, b) { 
        var t = "a"; 
        var Yb = "+"; 
        for (var c = 0; c < b.length - 2; c += 3) { 
            var d = b.charAt(c + 2), 
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
        } 
        return a 
    } 
    """)
        return ctx

    def buildUrl(self,text ,tk, sl,tl):
        baseUrl = 'http://translate.google.cn/translate_a/single'
        baseUrl += '?client=webapp&'  #这里client改成webapp后翻译的效果好一些 t翻译的比较差 ..
        baseUrl += 'sl=auto&'
        baseUrl += 'tl=' + str(tl) + '&'
        baseUrl += 'hl=zh-CN&'
        baseUrl += 'dt=at&'
        baseUrl += 'dt=bd&'
        baseUrl += 'dt=ex&'
        baseUrl += 'dt=ld&'
        baseUrl += 'dt=md&'
        baseUrl += 'dt=qca&'
        baseUrl += 'dt=rw&'
        baseUrl += 'dt=rm&'
        baseUrl += 'dt=ss&'
        baseUrl += 'dt=t&'
        baseUrl += 'ie=UTF-8&'
        baseUrl += 'oe=UTF-8&'
        baseUrl += 'clearbtn=1&'
        baseUrl += 'otf=1&'
        baseUrl += 'pc=1&'
        baseUrl += 'srcrom=0&'
        baseUrl += 'ssel=0&'
        baseUrl += 'tsel=0&'
        baseUrl += 'kc=2&'
        baseUrl += 'tk=' + str(tk) + '&'
        content=urllib.parse.quote(text)
        baseUrl += 'q=' + content
        return baseUrl

    def getHtml(self, session, url, headers):
        try:
            html = session.get(url, headers=headers)
            return html.json()
        except Exception as e:
            return None

    def translate(self, from_lan, to_lan, text):
        tk = self.getTk(text)
        url = self.buildUrl(text, tk, from_lan, to_lan)
        result = self.getHtml(self.session, url, self.headers)
        if result != None:
            ans = []
            s=''
            for i in result[0]:
                if i[0]!=None:
                    s+=i[0]
            for i in s.split('\n'):
                ans.append(i)
            return ans
        else:
            self.logger.info('谷歌翻译失败 ')
            return None

if __name__ == '__main__':

    gg = Google()
    text = '你好， 新的我'
    print(gg.translate('zh-CN', 'en', text))

