# Translator 🎉😁🐺
## 互联网在线翻译引擎爬虫集合
包含谷歌翻译、百度翻译、有道翻译、必应翻译、小牛翻译、腾讯翻译君等引擎。
Internet online translation engine crawler collection, including Google translation, Baidu translation, Youdao translation, Bing translation, Xiaoniu translation, Tencent translation Jun and other engines.

### 使用方法
每个翻译爬虫都包含一个translate方法，需要传入翻译文本、源语种和目标语种，返回翻译结果。
源语种和目标语种的缩写每个引擎都不一样，如需要其他语种翻译请自行查找引擎语种缩写。

### 破解方法
现在的翻译引擎基本上都使用了动态数据发送形式，用户输入文本之后由浏览器向后台服务器发送数据请求，返回包含翻译结果的数据包。

- 编写爬虫就是要模仿浏览器向翻译引擎后台服务器发送请求，接收并解析服务器返回的结果。
翻译引擎都会在发送的数据包中嵌入一些密匙数据用来确保数据是正常通过浏览器发送过来的，这些密匙通常由复杂的js代码生成，破解js加密代码是编写翻译爬虫的核心。
详情可以阅读百度、谷歌翻译的爬虫代码。
### 其他
对于爬虫经常被封禁的问题，大家可以尝试设置数据请求间隔，更换请求数据头User-Agent，或者使用代理解决。

### 参考
推荐大家一些爬虫教程，对于解析使用动态数据发送形式的网站很有用
Python实战教程：用Python破解有道JS加密
https://www.bilibili.com/video/av54049958/?spm_id_from=333.788.videocard.0
百度翻译加密js破解
https://www.cnblogs.com/jason-Gan/p/10567018.html

爬虫代码仅供学习交流使用，谢谢大家😄
