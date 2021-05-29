import urllib.request

def load_data():
    url = "http://www.baidu.com/"
    #GET请求
    #http请求
    #response：http响应对象
    response = urllib.request.urlopen(url)
    #print(response)
    #读取内容 byte类型
    data = response.read()
    #print(data)
    #将文件获取的内容转换为字符串
    str_data = data.decode("UTF-8")
    #print(str_data)
    #将数据写入文件
    with open("baidu.html", "w", encoding="utf-8") as f:
        f.write(str_data)
    #将字符串类型传唤为bytes
    str_name = "baidu"
    bytes_name = str_name.encode("utf-8")
    print(str_name)


load_data()
