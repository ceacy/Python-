number='13521082700'
#方法一：切片
#code='*'*4+" "+'*'*3+" "+number[-4:]
#方法二：replace方法
code=number.replace(number[0:7],'*'*7)
print("手机号: "+code)