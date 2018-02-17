@echo off 
start python3 networkMoni.py
rem 使用ping命令暂停3s，这样可以看到调用python后的结果
ping -n 3 127.0.0.1 > nul 
