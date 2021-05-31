import urllib.request

def proxy_user():

    proxy_list = [
        {"http": "104.131.109.66:8080"},
        {"http": "88.198.24.108:8080"},
        {"http": "96.113.165.182:3128"},
        {"http": "117.185.17.151:80"},
        {"http": "112.30.164.18:80"},

    ]
    for proxy in proxy_list:
        print(proxy)
        #利用遍历出来的IP创建处理器
        proxy_handler = urllib.request.ProxyHandler(proxy)
        #创建openner
        openner = urllib.request.build_opener(proxy_handler)

        try:
            openner.open("http://www.baidu.com", timeout=1)
            print("s1mpL3")
        except Exception as e:
            print(e)


proxy_user()