import urllib.request

def handler_openner():

    #系统的urlopen没有添加代理的功能，需要我们自定义该功能
    #安全 套接层 ssl第三方的CA数字证书
    #http:80
    #https:443
    #urlopen为什么可以请求数据：
    #①handler处理器，
    #②自己的openner请求数据
    url = "https://www.cnblogs.com/3cH0-Nu1L/"

    #创建自己的处理器
    handler = urllib.request.HTTPHandler
    #创建自己的oppener
    openner = urllib.request.build_opener(handler)
    #用自己创建的openner调用open方法请求数据
    response = openner.open(url)
    data = response.read()
    print(response)
    print(data)


handler_openner()