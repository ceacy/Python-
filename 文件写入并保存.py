import sys
import os

file = open(r'C:\\Ceacy工作\\test.txt','w')
file.write('hello world!2')
# 文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法
file.flush()
file.close()

