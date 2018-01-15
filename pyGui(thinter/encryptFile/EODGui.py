#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 0:26
# @Author  : Wendyltanpcy
# @File    : EODGui.py
# @Software: PyCharm

import tkinter as tk
import encryptFile as eF
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.ef = eF.eF()
        self.create_widgets()
    def create_widgets(self):

        #hint label1
        self.label1  = tk.Label()
        self.label1["text"] = "Please enter your file path here:"
        self.label1.grid(row=0,column=0)

        #hint label2
        self.label2 = tk.Label()
        self.label2["text"] = "Current key: "
        self.label2.grid(row=1,column=0)

        # hint label3
        self.label3 = tk.Label()
        self.label3["text"] = "Current file content: "
        self.label3.grid(row=2, column=0)


        #file path stringvar
        self.fileString = tk.StringVar()
        self.fileString.set("")

        #file key stringvar
        self.fileKey = tk.StringVar()
        self.fileKey.set(self.ef.get_fileKey())

        # file content stringvar
        self.fileContent = tk.StringVar()
        self.fileContent.set("")

        #file path entry
        self.editText1 = tk.Entry()
        self.editText1["textvariable"] = self.fileString
        self.editText1.grid(row=0,column=1)


        #file key entry
        self.editText2 = tk.Entry()
        self.editText2["textvariable"] = self.fileKey
        self.editText2.grid(row=1,column=1)

        # file content entry
        self.editText3 = tk.Entry()
        self.editText3["textvariable"] = self.fileContent
        self.editText3.grid(row=2, column=1,columnspan=4)

        #confirm button
        self.button_confirm = tk.Button()
        self.button_confirm["text"] = "confirm"
        self.button_confirm.bind("<ButtonPress>",self.read_filename)
        self.button_confirm.grid(row=0,column=2,columnspan="3")

        #encrypt button
        self.encrypt_btn = tk.Button()
        self.encrypt_btn["text"] = "encrypt"
        self.encrypt_btn.bind("<ButtonPress>", self.eord_file)
        self.encrypt_btn.grid(row=1, column=2)

        # decrypt button
        self.decrypt_btn = tk.Button()
        self.decrypt_btn["text"] = "decrypt"
        self.decrypt_btn.bind("<Button>", self.eord_file)
        self.decrypt_btn.grid(row=1, column=3)


    #thinter widget function
    def read_filename(self,event):
        message = self.ef.read_file(self.editText1.get())
        if message == "damn":
            messagebox.showwarning("warning!","Wrong or invalid file path!try again")
        elif message == "no file":
            messagebox.showinfo("no file","Have you enter anything to the path box yet?")
        else:
            self.read_content(event)

    def eord_file(self,event):
        if event.widget["text"]=="encrypt":
            self.ef.encrypt_or_decrypt('1', self.ef.get_fileName())
        elif event.widget["text"] == "decrypt":
            message = self.ef.encrypt_or_decrypt('2', self.ef.get_fileName())
            if message == "wrong key":
                messagebox.showwarning("wrong key!","The original key doesn't exist and the file decrypt fail")
                #representing decrypt fail.
                exit(1)
        self.read_content(event)

    def read_content(self,event):
        self.fileContent.set(self.ef.get_fileContentString())



if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.master.title("EOD file gui")
    app.master.maxsize(1000, 400)
    app.mainloop()