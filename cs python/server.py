#!/bin/env python

import socket
import sqlite3


def show_normal(cursor):
    cursor.execute('SELECT * FROM user')
    values = cursor.fetchall()
    content = ""
    for value in values:
        content += "\n"+",".join(value) + " "
    return content

def insert_and_show(conn,cursor,number,name):
    cursor.execute("INSERT INTO user (id,name) VALUES ('%s','%s')" % (number, name))
    conn.commit()
    return show_normal(cursor)

def update_and_show(conn,cursor,row,newname):
    cursor.execute("update user set name='%s' where id = %s" %(newname,row))
    conn.commit()
    return show_normal(cursor)

def delete_and_show(conn,cursor,row):
    cursor.execute("delete from user where id = %s" %row)
    conn.commit()
    return show_normal(cursor)

def string_to_bytecode(content,cfd):
    bytecode = bytes(content, encoding="utf8")
    cfd.send(bytecode)

def bytecode_to_string(cfd):
    buf = cfd.recv(1024)
    infos = str(buf, "utf8")
    return infos

def connect_database():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    print("db connect success!")
    return conn,cursor

def bind_address():
    address = ('127.0.0.1', 3138)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(address)
    s.listen(10)
    print("server connect!")
    return s

def delete_table_user(conn,cursor):
    cursor.execute("drop table user")
    cursor.close()
    conn.commit()
    conn.close()
    print("Delete table success!")

def main_fun():
    # doing database connection
    conn, cursor = connect_database()
    # bind address
    s = bind_address()
    #receive or send message
    while True:
        cfd,address=s.accept()
        receiveContent = bytecode_to_string(cfd)
        if(receiveContent=='y'):
            info ="What do you want to do?(1 select/2 insert/3 update/4 delete"
            cfd.send(info.encode())

        #get send back choice
        choice = bytecode_to_string(cfd)
        #handle different choices
        if(choice=="1"):
            #show data
            content = show_normal(cursor)
            string_to_bytecode(content,cfd)

        elif(choice=="2"):
            #insert data
            content = show_normal(cursor)
            string_to_bytecode(content, cfd)
            info = "Enter id and name:"
            cfd.send(info.encode())

            infos = bytecode_to_string(cfd)
            list = "".join(infos)
            id1 = list[0]
            name1 = list[2:]
            content = insert_and_show(conn,cursor,id1,name1)
            string_to_bytecode(content,cfd)

            print("S:Insert success!")
        elif(choice=="3"):
            #update data
            content = show_normal(cursor)
            string_to_bytecode(content, cfd)
            info = "Which row do u want to update?:"
            cfd.send(info.encode())

            infos = bytecode_to_string(cfd)
            list = "".join(infos)
            row1 = list[0]
            name1 = list[2:]
            content = update_and_show(conn,cursor,row1,name1)
            string_to_bytecode(content, cfd)
            print("S:Update success!")
        elif(choice=="4"):
            content = show_normal(cursor)
            string_to_bytecode(content, cfd)
            info = "Which row do u want to delete?:"
            cfd.send(info.encode())

            infos = bytecode_to_string(cfd)
            list = "".join(infos)
            row1 = list[0]
            content = delete_and_show(conn,cursor,row1)
            string_to_bytecode(content, cfd)
            print("Delete success!")
    # elif(choice=="5"):
    #     delete_table_user(conn,cursor)
        cfd.close()


if __name__ == '__main__':
    main_fun()







