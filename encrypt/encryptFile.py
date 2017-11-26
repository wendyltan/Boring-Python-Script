#! /usr/bin/python
'''
    File encryptFile.py
    Author: Wendy
    Date created: 11/26/2017
    Python Version: 3.5
    a script that can encrypt and decrpy your file.send your secret file and key to your friend to decrpt it!
'''

from cryptography.fernet import Fernet
import os
def encrypt_file(filename):
    # to encrypt
    data = ""
    file = open(filename, 'r')
    filedata = file.read()
    for line in filedata:
        data += line
    file.close()
    print("before encryped: \n" + data)
    encrypted_text = cipher.encrypt(bytes(data, encoding='utf8'))
    file = open(filename, 'wb')
    file.write(encrypted_text)
    file.close()
    print("encrypt success!")

def decrypt_file(filename):
    # to decrypt
    ddata = ""
    file = open(filename,'r')
    filedata = file.read()
    for line in filedata:
        ddata += line
    file.close()
    decrypted_text = cipher.decrypt(bytes(ddata,encoding='utf8'))
    file = open(filename, 'wb')
    file.write(decrypted_text)
    file.close()
    print("decrypt success!")

if __name__ == '__main__':

    cipher = Fernet(Fernet.generate_key())
    #if no key
    if  not os.path.isfile("key.txt"):
        # create cipher_key
        cipher_key = Fernet.generate_key()
        cipher = Fernet(cipher_key)
        # create encrypt object
        print(cipher_key)
        file = open("key.txt",'wb')
        file.write(cipher_key)
        file.close()
    #read key from file
    else:
        file = open("key.txt", 'rb')
        cipher_key =  file.read()
        print("key detected！\n"+str(cipher_key))
        cipher = Fernet(cipher_key)


    #read file
    filename = input("Please enter filename\n")
    if filename == "":
        print("No file in!")
        exit(0)
    choice = input("Input number 1 for encrypt or 2 for decrypt\n")
    if choice=='1':
        try:
            encrypt_file(filename)
        except FileNotFoundError:
            print("Sorry but it doesn't seem to be the right file name or it doesn't exist..")
    elif choice=='2':
        try:
            decrypt_file(filename)
        except UnicodeDecodeError:
            print("Maybe this is not secret file?Come back after you encrypt it")
        except FileNotFoundError:
            print("Sorry but it doesn't seem to be the right file name or it doesn't exist..")







