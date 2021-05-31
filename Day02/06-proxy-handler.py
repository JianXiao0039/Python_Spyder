import urllib.request

def create_proxy_handler():
    url = "https://www.cnblogs.com/3cH0-Nu1L/"

    #添加代理
    proxy = {
        #免费IP的写法
        "http": "104.131.109.66:8080"
        
    }
    #代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)

    #创建自己的openner
    openner = urllib.request.build_opener(proxy_handler)
    #拿着代理IP发送请求
    data = openner.open(url).read()
    print(data)


create_proxy_handler()