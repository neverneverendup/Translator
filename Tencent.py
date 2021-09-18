import re
import time
import requests
def get_filter(text):
    if isinstance(text, list):
        text = ''.join(text)
    text = str(text)
    text = text.strip()
    filter_list = [
        '\r', '\n', '\t', '\u3000', '\xa0', '\u2002',
        '<br>', '<br/>', '    ', '	', '&nbsp;', '>>', '&quot;',
        '展开全部', ' '
    ]
    for fl in filter_list:
        text = text.replace(fl, '')
    return text

def get_qtv_qtk():
    api_url = 'https://fanyi.qq.com/api/reauth12f'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/73.0.3683.86 Safari/537.36', }

    res = requests.post(api_url, headers=headers)
    data = res.text
    fy_guid = res.cookies.get('fy_guid')
    reg = re.compile(r'"qtv":"(.*?)"')
    qtv = reg.search(data).group(1)
    reg = re.compile(r'"qtk":"(.*?)"')
    qtk = reg.search(data).group(1)

    return fy_guid, qtv, qtk

def getHtml(url,headers,data):

    try:
        html= requests.post(url=url,data= data,headers=headers)
        #print(html.text)
        datas = html.json()['translate']['records']
        if html!=None and datas != None :
            # 以文本的形式打印结果
            trans_result = ''.join([data['targetText'] for data in datas])
        return trans_result
    except Exception:
        return None

class TencentTrans(object):
    def __init__(self):
        self.api_url = 'https://fanyi.qq.com/api/translate'
        self.headers = {
            'Cookie': 'fy_guid=605ead81-f210-47eb-bd80-ac6ae5e7a2d8; '
                      'qtv=ed286a053ae88763; '
                      'qtk=wfMmjh3k/7Sr2xVNg/LtITgPRlnvGWBzP9a4FN0dn9PE7L5jDYiYJnW03MJLRUGHEFNCRhTfrp/V+wUj0dun1KkKNUUmS86A/wGVf6ydzhwboelTOs0hfHuF0ndtSoX+N3486tUMlm62VU4i856mqw==; ',
            'Host': 'fanyi.qq.com',
            'Origin': 'https://fanyi.qq.com',
            'Referer': 'https://fanyi.qq.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/73.0.3683.86 Safari/537.36', }

        self.fromlang = 'auto'
        self.text='国家主席习近平致信祝贺中日高级别人文交流磋商机制首次会议在东京召开。习近平强调，当前，中日关系持续改善向好。希望中日双方共同利用好这一机制，推动人文交流，促进民心相通，为构建和发展契合新时代要求的中日关系提供人文支撑。'
        self.tolang = 'en'  # 设置默认为英语
        self.sessionUuid = str(int(time.time() * 1000))

        self.fy_guid, self.qtv, self.qtk = get_qtv_qtk()

        self.headers['Cookie'] = self.headers['Cookie'].replace(
            '605ead81-f210-47eb-bd80-ac6ae5e7a2d8', self.fy_guid)

        self.headers['Cookie'] = self.headers['Cookie'].replace(
            'ed286a053ae88763', self.qtv)
        self.headers['Cookie'] = self.headers['Cookie'].replace(
            'wfMmjh3k/7Sr2xVNg/LtITgPRlnvGWBzP9a4FN0dn9PE7L5jDYiYJnW03MJLRUGHEFNCRhTfrp/V+wUj0dun1KkKNUUmS86A/wGVf6ydzhwboelTOs0hfHuF0ndtSoX+N3486tUMlm62VU4i856mqw==',
            self.qtk)

    def get_trans_result(self,text):
        data = {
            'source': self.fromlang,
            'target': self.tolang,
            'sourceText': text,
            'qtv': self.qtv,
            'qtk': self.qtk,
            'sessionUuid': self.sessionUuid, }

        trans_result = getHtml(self.api_url,self.headers,data)
        return trans_result

if __name__ == '__main__':
    Tencent = TencentTrans()
    text = '你好'
    print(Tencent.get_trans_result(text))
