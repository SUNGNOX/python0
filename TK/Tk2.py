'''''2.��Frame�����Widget'''
# -*- coding: cp936 -*-
from tkinter import *
root = Tk()
fm = []
#�Բ�ͬ����ɫ�������frame
for color in ['red','blue']:
    #ע���������Frame�ķ��������������ؼ��ķ�����ͬ����һ����������root
    fm.append(Frame(height = 200,width = 400,bg = color))
#�������Frame�����һ��Label
Label(fm[1],text = 'Hello label').pack()
fm[0].pack()
fm[1].pack()
root.mainloop()
#Label����ӵ������Frame���ˣ�������rootĬ�ϵ����Ϸ���
#�󲿷ֵķ�������gm,��������gmʱ�ٽ���