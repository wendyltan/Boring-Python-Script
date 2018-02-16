#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/15 16:45
# @Author  : Wendyltanpcy
# @File    : networkMoni.py
# @Software: PyCharm
import multiprocessing
import psutil
import requests
import time
import ctypes,sys
import random
import math

STD_OUTPUT_HANDLE = -11

# Windows CMD命令行 字体颜色定义 text colors
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_RED = 0x0c # red.

# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

#set cmd color
def set_cmd_text_color(color,handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
def set_random_color():
    r = lambda: random.randint(0, 255)
    ran_color = '#%02X%02X%02X' % (r(), r(), r())
    return ran_color

#reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED|FOREGROUND_BLUE|FOREGROUND_GREEN)


#auto convert byte
def convertBytes(bytes):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if bytes >= prefix[s]:
            value = float(bytes) / prefix[s]
            return '%.2f %s' % (value, s)
    return '%.2f B' % (bytes)

#request to test net status
def run_request():
    while(True):
        try:
            #the site used for request test
            result = requests.get("http://www.baidu.com")
            code = str(result.status_code)
            reason = str(result.reason)
            mess = "status "+code + ' ' +reason+'\n'
        except requests.exceptions.ConnectionError:
            mess = "套接字操作尝试一个无法连接的主机"+'\n'
        except Exception:
            mess = "Something went wrong"+'\n'
        finally:


            before_byte_sent = psutil.net_io_counters(pernic=True)['WLAN'].bytes_sent
            before_byte_recv = psutil.net_io_counters(pernic=True)['WLAN'].bytes_recv

            #sleep for 1 sec
            time.sleep(1)

            after_byte_sent = psutil.net_io_counters(pernic=True)['WLAN'].bytes_sent
            after_byte_recv = psutil.net_io_counters(pernic=True)['WLAN'].bytes_recv

            sent_sec = str(convertBytes(after_byte_sent-before_byte_sent))
            recv_sec = str(convertBytes(after_byte_recv-before_byte_recv))


            #speed per sec
            byte_msg = "Total sent: " + sent_sec + '/s\n' + \
                       "Total receive: " + recv_sec + '/s\n'

            set_cmd_text_color(set_random_color())
            sys.stdout.write("=" * (int(byte_msg.__len__()/2))+'\n')

            sys.stdout.write(mess)
            sys.stdout.write(byte_msg)

            sys.stdout.write("=" * (int(byte_msg.__len__()/2))+'\n')

            resetColor()




if __name__ == '__main__':
    #start new process
    p = multiprocessing.Process(target=run_request,name="run request process")
    p.start()
    print(p.name+" "+str(p.pid)+" "+str(p.is_alive()))
    print("process start"+"\n")



