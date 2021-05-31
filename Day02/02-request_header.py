import urllib.request

def load_baidu():
    url = "http://www.baidu.com/"
    header = {
        # 浏览器版本
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "3cH0 - Nu1L": "s1mpL3",

    }
    #创建请求对象
    request = urllib.request.Request(url)
    #动态添加hander信息
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36")
    #请求网络数据
    response = urllib.request.urlopen(request)
    #print(response)
    data = response.read().decode("utf-8")
    #获取完整的url
    final_url = request.get_full_url()
    print(final_url)

    #获取请求头的信息
    #request_header = request.headers
    #print(request_header)
    #with open("02header.html", "w")as f:
    #    f.write(data)


load_baidu()