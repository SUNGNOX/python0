# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.quit)
        self.alertButton.pack()
app = Application()
 # 设置窗口标题:
app.master.title('Hello World')
 # 主消息循环:
app.mainloop()
