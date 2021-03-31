# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:39:19 2021

@author: byzjz
"""


'''
Tk类
代表绝大多数应用程序主窗口的高层空间

标签
用于说明一些文字信息，不需要执行任何功能，只是用来显示信息

按钮和功能的绑定
1、在按钮组件被声明的时候用command属性声明，command属性接收一个函数名
2、使用bind方法
bind可以接收三个参数
第一个参数是事件类型
第二个参数是一个函数名(不要加任何标点符号)，该函数必须接收一个参数，即表示该事件(event)

布局
pack布局
side

'''

'''
from tkinter import*
#对Tk这个类进行实例化，root是其一个实例
root=Tk()
root.wm_title("数据标注软件")
#w1是一个label的实例，有一个text属性，用来指定它的文本内容
w1=Label(root,text="股票评论")
#pack将label选择一个合适位置进行放置
w1.pack()
#事件循环
root.mainloop()
'''

from tkinter import*
def newLabel(event):
    global newtag
    s=Label(newtag,text="股票评论")
    s.pack()

newtag=Tk()
#command绑定按钮
#b1=Button(newtag,text="获取评论",command=newLabel)
b1=Button(newtag,text="获取评论")
b1.bind("<Button-1>",newLabel)
b1.pack()

newtag.mainloop()