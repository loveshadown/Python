#__* coding:utf-8 __*__

#引入正则表达式的包
import re



#创建一个正则表达式对象
pattern = re.compile('\d+\.\d+')


#提供要匹配的源字符串
src="2.11,3.22,4.222,4"
resource = pattern.findall(src)
print resource