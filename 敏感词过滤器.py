# 定义一个text_filter的函数，传入参数word、cencored_word和changed_word实现过滤，
# 敏感词cencored_word默认为'lame',替换词changed_word默认为'Awesome'
# 文件操作：open()、.write、.close()、
# 写入模式W：如果没有就在该路径创建一个有该名称文件，有则追加覆盖文本内容

def text_create(name,msg):
    desktop_path=r'C:\\Ceacy工作\\'
    full_path=desktop_path+name+'.xls'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')

#text_create('test2','hello new')

def text_filter(word,cencored_word='lame',changed_word='Awesome'):
    return word.replace(cencored_word,changed_word)

print(text_filter('python is lame!'))
