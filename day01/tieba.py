#_*_ coding:utf-8 _*_
#中文注释
import urllib2

def write_to_file(file_name,txt):
	'''
		将txt文本存到file_name文件
	'''
	#1 打开文件
	#2 读写文件
	#3 关闭文件
	f = open(file_name,'w')
	f.write(txt)
	f.close()



def tieba_spider(url,begin_page,end_page):
	'''
		贴吧小爬虫的方法
	'''
	for i in range(begin_page,end_page+1):
		pn = i

		#组成一个完整的url

		myurl = url + str(i)
		print myurl
		req = urllib2.Request(myurl)
		response = urllib2.urlopen(req)
		html = response.read()
		file_name = str(i) + ".html"
		write_to_file(file_name,html)



#main
if __name__ == "__main__":
	str11="请输入贴吧的URL地址"
	url = raw_input(str11)
	print url
	begin_page = int(raw_input("请输入起始页码"))
	end_page = int(raw_input("请输入种植页面"))
	print begin_page

	tieba_spider(url,begin_page,end_page)
