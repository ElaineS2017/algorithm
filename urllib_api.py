# -*- coding: utf-8 -*-
import urllib2

'''
    urlopen(url, data, timeout)
    url: 
    data: 访问url时要传送的数据，默认None
    timeout: 超时时间，t默认为 socket._GLOBAL_DEFAULT_TIMEOUT
    return: 返回一个response对象，返回信息便保存在这里面
'''
response = urllib2.urlopen("https://www.baidu.com/")
print response.read()
#response对象有一个read方法，可以返回获取到的网页内容
'''
    urlopen参数可以传入一个request请求,它其实就是一个Request类的实例，构造时需要传入Url,Data等等的内容
'''
request = urllib2.Request("https://www.baidu.com/")
response = urllib2.urlopen(request)
print response.read()

'''
    数据传送 POST,GET
    区别：
    GET：是直接以链接形式访问，链接中包含了所有的参数，当然如果包含了密码的话是一种不安全的选择，不过你可以直观地看到自己提交了什么内容
    POST：不会在网址上显示所有的参数，不过如果你想直接查看提交了什么就不太方便
'''
#POST
import urllib
import urllib2

values = {"username": "1231jodjqw", "password": "XXXX"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?ref=toolbar"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()
#或者
values = {}
values['username'] = "1231jodjqw"
values['password'] = "XXXX"
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?ref=toolbar"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()

#GET
import urllib
import urllib2

values = {}
values['username'] = "1231jodjqw"
values['password'] = "XXXX"
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?ref=toolbar"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)

'''
    设置Headers属性
    有些网站不会同意程序直接用上面的方式进行访问，如果识别有问题，那么站点根本不会响应，所以为了完全模拟浏览器的工作，我们需要设置一些Headers 的属性。
'''
url = "https://passport.csdn.net/account/login?ref=toolbar"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.0.0'
values = {"username": "1231jodjqw", "password": "XXXX"}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()

'''
对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应，所以我们还可以在headers中加入referer
'''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)',
    'Referer': 'https://www.zhihu.com/'}
#在传送请求时把headers传入Request参数里，这样就能应付防盗链了
'''
    User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
    Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
    application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
    application/json ： 在 JSON RPC 调用时使用
    application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
    在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
'''
'''
    Proxy（代理）的设置
    urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问。所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理
'''
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

'''
    Timeout 设置
    设置等待多久超时，为了解决一些网站实在响应过慢而造成的影响。
'''
#如果第二个参数data为空那么要特别指定是timeout是多少，写明形参，如果data已经传入，则不必声明。
import urllib2
response = urllib2.urlopen('http://cn.bing.com/', timeout=10)

response = urllib2.urlopen('http://cn.bing.com/', data, 10)
'''
http协议有六种请求方法，get,head,put,delete,post,options
PUT：这个方法比较少见。HTML表单也不支持这个。本质上来讲， PUT和POST极为相似，都是向服务器发送数据，但它们之间有一个重要区别，PUT通常指定了资源的存放位置，而POST则没有，POST的数据存放位置由服务器自己决定。
DELETE：删除某一个资源。基本上这个也很少见，不过还是有一些地方比如amazon的S3云服务里面就用的这个方法来删除资源。
'''
#如果要使用 HTTP PUT 和 DELETE ，只能使用比较低层的 httplib 库。虽然如此，我们还是能通过下面的方式，使 urllib2 能够发出 PUT 或DELETE 的请求，不过用的次数的确是少
import urllib2
request = urllib2.Request(url, data)
request.get_method = lambda: 'PUT'
response = urllib2.urlopen(request)

'''
    使用DebugLog
'''
#收发包的内容就会在屏幕上打印出来
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://cn.bing.com/')















