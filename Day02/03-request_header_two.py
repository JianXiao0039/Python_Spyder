import urllib.request

def load_baidu():
    url = "http://www.baidu.com/"
    header = {
        #浏览器版本
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "3cH0 - Nu1L": "s1mpL3",

    }
    #创建请求对象
    request = urllib.request.Request(url, headers=header)
    #请求网络数据(不在此处增加请求头信息，因为此方法系统没有提供参数)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

    #获取请求头的信息(所有头的信息)
    #request_headers = request.headers
    #print(request_headers)
    #第二种方式打印headers信息
    request_headers = request.get_header("User-agent")
    print(request_headers)
    with open("02header.html", "w")as f:
        f.write(data)


load_baidu()