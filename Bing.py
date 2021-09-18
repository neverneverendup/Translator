import urllib.request
import urllib.parse

class Bing(object):
    def __init__(self):
        self.url = "http://api.microsofttranslator.com/v2/ajax.svc/TranslateArray2?"

    def translate(self, from_lan, to_lan,content,):
        data = {}
        if from_lan != 'auto':
            data['from'] = '"' + from_lan + '"'
        data['to'] = '"' + to_lan + '"'
        data['texts'] = '["'
        data['texts'] += content
        data['texts'] += '"]'
        data['options'] = "{}"
        data['oncomplete'] = 'onComplete_3'
        data['onerror'] = 'onError_3'
        data['_'] = '1430745999189'
        data = urllib.parse.urlencode(data).encode('utf-8')
        strUrl = self.url + data.decode() + "&appId=%223DAEE5B978BA031557E739EE1E2A68CB1FAD5909%22"
        response = urllib.request.urlopen(strUrl)
        str_data = response.read().decode('utf-8')
        tmp, from_lang = str_data.split('"From":')
        from_lang = from_lang[1:from_lang.find('"', 1)]
        print("detected from_lang={}".format(from_lang))
        tmp, str_data = str_data.split('"TranslatedText":')
        translate_data = str_data[1:str_data.find('"', 1)]
        return translate_data

if __name__ == '__main__':

    content='hello'
    bing=Bing()
    print(bing.translate('en', 'zh',content))



