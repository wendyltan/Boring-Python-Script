#coding:utf-8
from PIL import ImageGrab  #导入截图模块
import time


choose = raw_input("Enter y for screenshot or q for quit:\n")

while choose is 'y': 
        pic = ImageGrab.grab()  #截图（这就截取好了，是全屏哦）
        timeTemp = time.time() #1970纪元后经过的浮点秒数，得到时间戳
        timeTempNext = time.localtime(timeTemp) #将一个时间戳转换成一个当前时区的struct_time（自己可以看一下这个结构和C++的差不多）
        timeNow = time.strftime("%Y-%m-%d-%H-%M-%S", timeTempNext) #将此时的struct_time，根据指定的格式化字符串输出
        print "the time stamp is:"+timeNow
        savePath = timeNow + ".jpg"#字符串的合并生产合理的路径
        pic.save(savePath)#保存图片
        print "pic save success!\n"
        choose = raw_input("Enter y for screenshot or q for quit:\n")

if choose is 'q':
    print "program end!"