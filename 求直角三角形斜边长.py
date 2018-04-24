#中级难度：设计一个求直角三角形斜边长的函数（两条直角边为参数，求最长边）
#math.sqrt( x ) :返回x的平方根
import math
def triangle(arg1,arg2):
     return "The right triangle third side's length is {}".format(math.sqrt(arg1**2+arg2**2))


print (triangle(3,4))