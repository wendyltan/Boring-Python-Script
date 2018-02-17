#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/15 16:45
# @Author  : Wendyltanpcy
# @File    : networkMoni.py
# @Software: PyCharm
import multiprocessing
import psutil
import requests
import ctypes
import random
import click
import time


STD_OUTPUT_HANDLE = -11

# Windows CMD命令行 字体颜色定义 text colors
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_RED = 0x0c # red.

global_url = "www.baidu.com"
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


@click.command()
@click.option('--url',default=global_url,help='Set url of test request')
def setUrl(url):
    global global_url
    global_url = url
    start_process()


def set_cmd_text_color(color,handle=std_out_handle):
    """set cmd text color"""
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
def set_random_color():
    """give it a random color"""
    r = lambda: random.randint(0, 255)
    ran_color = '#%02X%02X%02X' % (r(), r(), r())
    return ran_color

#reset white
def resetColor():
    """reset cmd color to white"""
    set_cmd_text_color(FOREGROUND_RED|FOREGROUND_BLUE|FOREGROUND_GREEN)

def convertBytes(bytes):
    """automatically convert byte into readable byte info"""
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
    """do main request loop here to check the net status"""
    while(True):
        try:
            #the site used for request test
            result = requests.get("http://"+global_url,timeout=1)
            code = str(result.status_code)
            reason = str(result.reason)
            server = str(result.headers["Server"])
            mess = "Status "+code + ' ' +reason + '\n'+"Request Server: "+server
        except requests.exceptions.ConnectionError:
            mess = "套接字操作尝试一个无法连接的主机"+'\n'
        except requests.exceptions.HTTPError:
            mess = "Unsuccess status code"+'\n'
        except requests.exceptions.Timeout:
            mess = "Request time out"+'\n'
        finally:
            before_byte_sent = psutil.net_io_counters(pernic=True)['WLAN'].bytes_sent
            before_byte_recv = psutil.net_io_counters(pernic=True)['WLAN'].bytes_recv
            before_package_sent = psutil.net_io_counters(pernic=True)['WLAN'].packets_sent
            before_package_recv = psutil.net_io_counters(pernic=True)['WLAN'].packets_recv

            #sleep for 1 sec
            time.sleep(1)

            after_byte_sent = psutil.net_io_counters(pernic=True)['WLAN'].bytes_sent
            after_byte_recv = psutil.net_io_counters(pernic=True)['WLAN'].bytes_recv
            after_package_sent = psutil.net_io_counters(pernic=True)['WLAN'].packets_sent
            after_package_recv = psutil.net_io_counters(pernic=True)['WLAN'].packets_recv

            sent_sec = str(convertBytes(after_byte_sent-before_byte_sent))
            recv_sec = str(convertBytes(after_byte_recv-before_byte_recv))
            package_sent_sec = str(after_package_sent - before_package_sent)
            package_recv_sec = str(after_package_recv - before_package_recv)


            #speed per sec
            byte_msg = "Total sent: " + sent_sec + '/s\n' + \
                       "Total receive: " + recv_sec + '/s'

            package_msg = "Package sent: " +package_sent_sec + "/s\n" + \
                          "Package receive: " + package_recv_sec + "/s"

            set_cmd_text_color(set_random_color())
            print("=" * (int(byte_msg.__len__()/2)))
            print(mess)
            print(byte_msg)
            print(package_msg)

            print("=" * (int(byte_msg.__len__()/2)))

            resetColor()


def start_process():
    """start a new process to request"""
    p = multiprocessing.Process(target=run_request, name="run request process")
    p.start()
    print(p.name + " " + str(p.pid) + " " + str(p.is_alive()))
    print("process start" + "\n")

if __name__ == '__main__':
    setUrl()





