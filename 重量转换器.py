#初级难度：设计一个重量转换器，输入以"g"为单位的数字后返回换算成"kg"的结果
def transfunc():
    number=input("请输入以g为单位的数字")
    result=int(number)/1000
    return str(result)+"kg"

print(transfunc())
