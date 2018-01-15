#! /usr/bin/python3
'''
    File encryptFile.py
    Author: Wendy
    Date created: 11/26/2017
    Python Version: 3.5
    a script that can encrypt and decrpy your file.send your secret file and key to your friend to decrpt it!
'''
import cryptography
from cryptography.fernet import Fernet
import os
import codecs

class eF():
    def __init__(self):
        super().__init__()
        self.read_key()
        self.filename=""
        self.content=""


    def encrypt_file(self,filename):
        # to encrypt
        data=""
        file = open(filename, 'r', encoding="utf8")
        filedata = file.read()
        for line in filedata:
            data += line
        file.close()
        encrypted_text = self.cipher.encrypt(bytes(data, encoding='utf8'))
        self.content = encrypted_text
        file = open(filename, 'wb')
        file.write(encrypted_text)
        file.close()
        print("encrypt success!")

    def decrypt_file(self,filename):
        # to decrypt
        data=""
        file = open(filename, 'r', encoding="utf8")
        filedata = file.read()
        for line in filedata:
            data += line
        file.close()
        try:
            decrypted_text = self.cipher.decrypt(bytes(data, encoding='utf8'))
            self.content = decrypted_text
            file = open(filename, 'wb')
            file.write(decrypted_text)
            file.close()
            print("decrypt success!")
        except cryptography.fernet.InvalidToken:
            return "wrong key"


    def read_key(self):
        self.cipher = Fernet(Fernet.generate_key())
        # if no key
        if not os.path.isfile("key.txt"):
            # create cipher_key
            cipher_key = Fernet.generate_key()
            self.cipher = Fernet(cipher_key)
            # create encrypt object
            print(cipher_key)
            self.key = cipher_key
            file = open("key.txt", 'wb')
            file.write(cipher_key)
            file.close()
        # read key from file
        else:
            file = open("key.txt", 'rb')
            cipher_key = file.read()
            print("key detected！\n" + str(cipher_key))
            self.cipher = Fernet(cipher_key)
            self.key = cipher_key


    def read_file(self,filename):
        # read file
        self.filename = filename
        try:
            if filename == "":
                print("No file in!")
                return "no file"
            else:
                print(self.filename)
                data = ""
                file = open(filename, 'r', encoding="utf8")
                filedata = file.read()
                for line in filedata:
                    data += line
                file.close()
                self.content = data
        except FileNotFoundError:
            return "damn"


    def get_fileContentString(self):
        return self.content

    def get_fileKey(self):
        return self.key

    def get_fileName(self):
        return self.filename


    def encrypt_or_decrypt(self,choice,filename):
        if choice == '1':
            try:
                self.encrypt_file(filename)
            except FileNotFoundError:
                print("Sorry but it doesn't seem to be the right file name or it doesn't exist..")
        elif choice == '2':
            try:
                message = self.decrypt_file(filename)
                return message
            except UnicodeDecodeError:
                print("Maybe this is not secret file?Come back after you encrypt it")
            except FileNotFoundError:
                print("Sorry but it doesn't seem to be the right file name or it doesn't exist..")













