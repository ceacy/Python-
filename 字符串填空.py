city=input("请输入城市名称")
url="http://apistore.baidu.com/microservice/weather?citypingin={}".format(city)
print(url)