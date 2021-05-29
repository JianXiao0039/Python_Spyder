import urllib.request
import urllib.parse
import string

def get_method_params():
    url = "http://www.baidu.com/s?wd="
    #拼接字符串(汉字)
    name = "爬虫"
    final_url = url + name
    print(final_url)
    #代码发送了请求
    #网址里面包含了汉字；ascii是没有汉字的；URL转义
    #将包含汉字的网址进行转义
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    response = urllib.request.urlopen(encode_new_url)
    print(response)
    #读取内容
    data = response.read().decode()
    print(data)
    #保存到本地
    with open("encode_test.html", "w", encoding="utf-8")as f:
        f.write(data)
    #UnicodeEncodeError: 'ascii' codec can't encode characters in position 15-16: ordinal not in range(128)
    #针对报错结合上一条注释的解释：
    #python是解释性语言；解释器只支持 ascii 0 - 127，即不支持中文！！！


get_method_params()