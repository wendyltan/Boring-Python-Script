#!/bin/env python
import socket 
import time



def show_server_message(s):
    serverBack = str(s.recv(1024), "utf8")
    print("S: " + serverBack)

def send_info_with_hint(s,hint):
    info = input(hint)
    s.send(info.encode())

def deal_with_choice(choice,s,hint):
    s.send(choice.encode())
    show_server_message(s)
    show_server_message(s)
    send_info_with_hint(s,hint)
    show_server_message(s)

def main_fun():
    i = 1
    while i < 10:
        # connect the address
        address = ("127.0.0.1", 3138)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        # send first request
        request = input("asking for request?(y/n)")
        if request == "y":
            s.send(request.encode())
        else:
            s.close()
            print("Server close... thanks for using!")
            break

        # getting data from server
        show_server_message(s)
        choice = input("enter choice here>>")
        if (choice == "1"):
            s.send(choice.encode())
            show_server_message(s)
        elif (choice == "2"):
            deal_with_choice(choice, s, "enter id and name here(id name)>>")
        elif (choice == "3"):
            deal_with_choice(choice, s, "enter new info here(row new_name)>>")
        elif (choice == "4"):
            deal_with_choice(choice, s, "enter delete row here(delete_row)>>")

        s.close()
        time.sleep(1)
        i += 1


if __name__ == '__main__':
    main_fun()
