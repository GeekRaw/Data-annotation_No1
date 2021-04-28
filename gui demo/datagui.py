# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:39:37 2021

@author: byzjz
"""


"""
button
b1=button(windows,text,command)
command绑定事件

创建一个新窗口
win=tkinter.Tk() 创建窗口
win.geometry("600x400"+300+200) 设置窗口的位置及大小
win.mainloop() 进入消息循环

布局
pack(pack先依照side命令进行排布，再按照anchor进行对齐)
相关参数
side:组件的排布方式
left,right,top,buttom

anchor 组件的对齐方式
n(上边),s(下边)，w(左边)，e(右边),nw(左上角),ne(右上角),sw(左下角),se(右下角),center(中心)
ipadx x方向的内边距  ipady y方向的外边距
padx x方向的外边距  pady y方向的外边距

label参数
label(master,option...)

master：框架的父容器
bg:标签背景色
cursor，鼠标移动到标签时，光标的形状(可设置为arrow,circle,cross,plus)
front 设置字体
text 设置文本
width 设置标签的宽度
height 标签的高度
padx x轴间距
pady y轴间距
fill x 横向填充 y 纵向填充  both 横向和纵向都填充

place()布局
anchor定义控件在窗体内的方位
in 此选项定义控件相对于参考控件的位置
x 定义控件的绝对水平位置
y 定义控件的绝对垂直位置
(x,y)即为距离窗体左上角的坐标

grid()布局

输入框
Entry

如果设置菜单选项的大小?

add_command
add_commnd添加菜单项
如果该菜单是顶层菜单，则添加的菜单以此向右添加
如果该菜单是顶层菜单的一个菜单项，则添加的是下拉菜单

add_command参数
label 指定菜单项的名称
command  指定被点击时调用的方法
acceletor 指定快捷键
underline  指定是否有下划线

add_cascade 添加子菜单
add_cascade的作用是为了引出后面的菜单

add_cascade参数
menu  指定把某个菜单级联到该菜单项上
label  指定该菜单项的名称

控件的command参数要通过 command=lambda:的形式传参数
调用window.quit退出窗口

弹出菜单 Menu中的post方法，接受两个参数，即x和y坐标，会在相应的位置弹出菜单

canvas create_arc绘制扇形
create_arc参数
canvas.create_arc(coord,start,extent,fill)

coord元组设置矩形所形成的椭圆的左上角坐标及右下角坐标:
coord=x1,y1,x2,y2

start 从x轴正方向(起始方向)开始，单位未度进行绘制，start为起始绘制角度的设置
extent：以start参数作为参考，以start参数给定的角度开始，逆时针延伸角度，这个角度为extent设置的值
fill：设施绘制区域的填充颜色 fill="red"

create_text  画布上添加文字信息
create_text(x,y,text) x,y为文字信息的坐标

定义了画布后，图形的起始和结束坐标是相对与画布的，而不是相对于窗体

scrollbar滚动条
scrollbar(master,option)

orient 指定绘制"horizontal"(垂直滚动条) "vertical"(水平滚动条)





radiobutton 单选按钮
单选按钮组件用于实现多选一的问题，每一个单选按钮都可以与以一个python的函数或方法与之相关联
当按钮按下的时，对应的函数或方法将被自动执行
每一组单选按钮组件应该只与一个变量相关联，然后每一个按钮表示该变量的单一值

参数
radiobutton(master,options)

组件选项：
command 指定该按钮相关联的函数或方法
value 1 标志该单选按钮的值 2 在同一组中的所有按钮应该拥有各不相同的值  
      3 通过将该值与variable选项的值对比，即可判断用户选中了哪个按钮

variable 1 同一组件中的所有按钮的variable选项应该都指向同一个变量
         2 通过该变量与value选项的值对比，即可判断用户选中了哪个按钮
         用于跟踪用户的选择，在所有radiobutton之间共享

单选按钮方法
deselect() 取消该按钮的选中状态
select() 将按钮设置为选中状态

message box
确认/取消对话框 askokcancel 
askokcancel(title,message,**options)
askokcancel返回布尔类型，点击确认返回true,点击取消返回false

鼠标事件
<Button-1> 鼠标左键
<Double-Button-1> 双击鼠标左键

listbox相关方法
curselection()
返回一个元组，包含被选中的选项的序号(从0开始)

delete(first,last=None)
删除参数first到last范围内(包含first和last)的所有选项
如果忽略last参数，表示删除first参数指定的选项

get(first,last=None)
返回一个元组，包含参数first到last范围内的所有选项的文本

python对可变对象(list,dict,set)采用引用传递的方式，对不可变对象(number,string,tuple)等，采用值传递
要在函数内修改外部的不可变对象，可以将其定义为全局对象(global)

批量删除
curselection()在多选模式下，返回一个元组，元组中是选定元素的下标，用户先进行选择，选择完后点击删除
获取curselection()返回的元组，逐个读出元组中的元素delete


正则表达式
.可以匹配除换行符之外的任何字符
*匹配前面的字符0次或多次

特殊字符: \.^$?+*{}[]()|
使用以上特殊字符的字面值，必须使用\进行转义

re.sub(x,s,m)
返回一个字符串，每个匹配的地方用x进行替换，返回替换后的字符串最多替换m次

文件读写
a :打开一个文件用于追加，如果该文件已存在，文件指针将会放在文件的结尾，即新的内容将会被写入到已有内容之后
如果该文件不存在，创建新文件进行写入
"""
from tkinter import*
from tkinter import ttk
from tkinter.filedialog import*
import tkinter
from tkinter.messagebox import askokcancel,showinfo,WARNING
import ast

#存放标签
tag_all=["标签1","标签2","标签3","标签4","标签5","标签6","标签7","标签8","标签9","标签10","标签11"]
#存放评论

comment=[]

 #评论下标,双击主界面某一评论时，更新该值
global comment_detail_index



#目录查询
def selectPath(new_path):
    
    _path=askdirectory()
    new_path.set(_path)
    #正确获取文件路径
    print(new_path.get())

#文件目录添加和文件添加
def create_file(new_path,new_folder):
    #接收用户输入数据打印
    #folder没有读取到数据?
    
    print(new_folder.get()) 
    print(new_folder)
    #print(new_path.get())
    
    #dirs = path.get()
    #file = open(dirs+'/'+folder.get(),"w")
    messagebox.showinfo("提示","文件创建成功")
        
#新建文件
def new_file():
    new_file_win=Tk()
    new_file_win.title("新建文件")
    new_file_win.geometry("300x150")
    
    #存储用户输入信息
    new_path=StringVar()
    new_folder=StringVar() 
    
    Label(new_file_win,text="目标路径").place(x=10,y=10)
    Entry(new_file_win,textvariable=new_path).place(x=70,y=10)
    Button(new_file_win,text="路径选择",command=lambda:selectPath(new_path)).place(x=220,y=10)
    
    
    Label(new_file_win,text="文件名").place(x=10,y=60)
    Entry(new_file_win,textvariable=new_folder).place(x=70,y=60)
    Button(new_file_win,text="确定",command=lambda:create_file(new_path,new_folder)).place(x=220,y=60)
    
    new_file_win.mainloop()
    


    
#文件导入
def importfile(lb):
    
    global filename
    filename=askopenfilename(defaultextension=".txt")
    if(filename==""):
        filename=None
    else:
        #root.title("导入"+os.path.basename(filename))
        #导入新的文件，先清空listbox和comment中的内容
        lb.delete(0,len(comment)-1)
        comment.clear()
        
        f=open(filename,"r")
        for line in f.readlines():
            #先将读出的字符串转成字典，再按照字段读出数据
            comment_dict=ast.literal_eval(line)
            
            comment.append(comment_dict['comment_text'])
            lb.insert("end",comment_dict['comment_text'])
        
        f.close()
        
    return filename
        
#文件保存      
def filesave():
    global filename
    try:
        f=open(filename,'w')
        #写入保存内容
        #f.write(msg)
        f.closed()
    except:
        filesaveas()
#文件另存为
def filesaveas():
    f=asksaveasfilename(initialfile="未命名.txt",defaultextension=".txt")
    global filename
    filename=f
    #存文件
  
            
#3个提示信息
def downloadMessage1(nwin):
    msg=Label(nwin,text="下载中...")#padx设置x方向内边距, pady设置y方向内边距
    msg.grid(row=2)
    
def downloadMessage2(nwin):
    msg=Label(nwin,text="下载停止")#padx设置x方向内边距, pady设置y方向内边距
    msg.grid(row=2)

def downloadMessage3(nwin):
    msg=Label(nwin,text="下载完毕")#padx设置x方向内边距, pady设置y方向内边距
    msg.grid(row=2)
    
#下载管理
def download():
    dwin=Tk()
    dwin.title("下载管理")
    dwin.geometry("400x200")
    label1=Label(dwin,text="股票代码")
    info1=Entry(dwin,font=('Arial',14))
    label1.grid(row=0,column=0)
    info1.grid(row=0,column=1)
    begin=Button(dwin,text="开始下载",command=lambda:downloadMessage1(dwin))
    begin.grid(row=1,column=0,padx=50,pady=50)
    end=Button(dwin,text="停止下载",command=lambda:downloadMessage2(dwin))
    end.grid(row=1,column=1,pady=50)
    
    dwin.mainloop()
    
#统计图
#用listbox存选项
#用循环画多个扇形
def datachart():
    cwin=Tk()
    cwin.title("统计图")
    cwin.geometry("500x500")
    
   
    tagchoice=ttk.Combobox(cwin)
    tagchoice['value']=('标签1','标签2','标签3')
    tagchoice.current(0)
    tagchoice.place(x=20,y=20,anchor='w')
    
    canvas_chart=Canvas(cwin,height=300,width=300) #设置画布样式
    canvas_chart.place(x=40,y=40)
    
    canvas_chart.create_arc(250,250,50,50,start=0,extent=240,fill="red")
    canvas_chart.create_arc(250,250,50,50,start=240,extent=120,fill="blue")
    
    canvas_yes=Canvas(cwin,height=25,width=25)
    canvas_yes.place(x=20,y=400)
    canvas_yes.create_rectangle(0,0,25,25,fill="red")
    label_yes=Label(cwin,text="是(66.7%)")
    label_yes.place(x=55,y=400)
    
    canvas_no=Canvas(cwin,height=25,width=25)
    canvas_no.place(x=20,y=435)
    canvas_no.create_rectangle(0,0,25,25,fill="blue")
    label_no=Label(cwin,text="否(33.3%)")
    label_no.place(x=55,y=435)
    
    cwin.mainloop()
    
#删除标签
def tag_delete(tag_listbox):
    tmp_tag=tag_listbox.curselection()
    tag_index=list(tmp_tag)
    tag_index.sort(reverse=True)
    print(tag_index)
    
    for item in tag_index:
        tag_listbox.delete(item)
        del tag_all[item]
    print(tag_all)

#新建标签
#第一个输入框输入标签
#第二个输入框输入标签的选项，后面有一个确认按钮，点击确认后添加到下方的listbox
#listbox展示全部的标签选项，点击鼠标右键可以删除选中的选项
#点击最下方的确认按钮后，创建成功，写入到保存标签的文件中，同时也加入到commet类中的label中

#确认标签名
tag_name=[]
def tag_name_confirm(entag):
    tag_name.clear()
    
    tag_name.append(entag.get())
    for item in tag_name:
        print(item)

#确认选项名
def tag_choice_confirm(enchoice,choicelist):
    choicelist.insert("end",enchoice.get())
    enchoice.delete(0,END)
#创建提示
def add_message():
    messagebox.showinfo('提示','创建成功')    
    
def choice_delete(even,choice):
    tmp=choice.curselection()
    print(tmp)
    index=tmp[0]
    choice.delete(index)
    
def tag_add():
    #创建一个字典保存当前创建的标签内容
    tag_tmp={}
    tag_add_win=Tk()
    tag_add_win.geometry("350x400")
    tag_add_win.title("新建标签")
    fm_tag_add=Frame(tag_add_win,width=350,height=85)
    fm_tag_choice=Frame(tag_add_win,width=350,height=85)
    fm_choice_list=Frame(tag_add_win,width=350,height=180)
    fm_add_confirm=Frame(tag_add_win,width=350,height=50)
    fm_tag_add.grid(row=0)
    fm_tag_choice.grid(row=1)
    fm_choice_list.grid(row=2)
    fm_add_confirm.grid(row=3)
    
    input_label=Label(fm_tag_add,text="标签")
    input_label.place(x=60,y=30)
    
    #输入标签
    input_tag=Entry(fm_tag_add)
    input_tag.place(x=95,y=30)
    #标签确认
    input_tag_button=Button(tag_add_win,text="确认",command=lambda:tag_name_confirm(input_tag))
    input_tag_button.place(x=250,y=25)
   
    
    input_choice=Label(fm_tag_choice,text="选项")
    input_choice.place(x=60,y=20)
    
    #输入选项
    input_choice=Entry(fm_tag_choice)
    input_choice.place(x=95,y=20)
    #选项确认
    #确认选项后添加到字典中
    choice_button=Button(fm_tag_choice,text="确认",command=lambda:tag_choice_confirm(input_choice,choice_list))
    choice_button.place(x=250,y=15)
    
    #listbox显示选项
    #滚动条
    choice_sc=Scrollbar(fm_choice_list)
    choice_sc.pack(side=RIGHT,fill=Y)

    #列表滚动，滚动条跟着滚动
    choice_list=Listbox(fm_choice_list,yscrollcommand=choice_sc.set)
    choice_list.pack(side=LEFT,fill=BOTH,expand=True)
    #右键删除选项
    choice_list.bind('<Button-3>',lambda event:choice_delete(event,choice_list))

    #滚动条动，列表跟着滚动
    choice_sc.config(command=comment_list.yview)
    
    #创建确认按钮
    #确认创建后，添加到文件中
    tag_confirm_button=Button(fm_add_confirm,text="确认",command=add_message)
    
    tag_confirm_button.place(x=160,y=10)
    

    
    tag_add_win.mainloop()
    
    
#标签管理
def tag():
    tag_win=Tk()
    tag_win.geometry("400x400")
    tag_win.title("标签管理")
   
    
    #使用listbox展示所有标签,listbox为多选模式
    #设置滚动条
    main_tag_sc=Scrollbar(tag_win)
    main_tag_sc.pack(side=RIGHT,fill=Y)

    #列表滚动，滚动条跟着滚动
    tag_listbox=Listbox(tag_win,width=100,height=15,selectmode=MULTIPLE,yscrollcommand=main_tag_sc.set)
    tag_listbox.pack(side=LEFT,fill=BOTH,expand=True)

    #滚动条动，列表跟着滚动
    main_tag_sc.config(command=tag_listbox.yview)
    
    for item in tag_all:
        tag_listbox.insert("end",item)
        
    menubar=Menu(tag_win)
    
    menubar.add_command(label='新建',command=tag_add)
    menubar.add_command(label='删除',command=lambda:tag_delete(tag_listbox))
    tag_win['menu']=menubar
    
    tag_win.mainloop()



    

def confirm():
    answer=askokcancel(title="删除标签",message="确认删除标签?",icon=WARNING)
    
#数据标注工作区,用两个frame管理,上半部分的frame放text显示数据，下半部分frame放多选按钮
#每次调用datasort的时候，将未标记的数据读入到工作区的列表中
def datasort():
    dswin=Tk()
    dswin.geometry("400x450")
    dswin.title("数据标注")
    
    menubar=Menu(dswin)
    menubar.add_command(label="已标注数据")
    menubar.add_command(label="未标注数据")
    
    fm_1=Frame(dswin,width=400,height=200)
    fm_2=Frame(dswin,width=400,height=200)
    fm_3=Frame(dswin,width=400,height=50)
    fm_1.pack()
    fm_2.pack()
    fm_3.pack()
   
    #读入未标记的数据
    
   
    text=Text(fm_1,width=380,height=15)
    text.pack()
    
   
    #text.delete('1.0','end') 每次读入一条新的评论时先清空text中的数据
    #读出每条评论插入到text中,使用update更新数据
    for i in range(1,1000):
        text.insert("end",i)
    
    #用一个list存标签
    tag1=Label(fm_2,text="是否推广贴")
    tag1.pack(side='left')
    v=IntVar()
    r1=Radiobutton(fm_2,text='是',variable=v,value=1)
   
    r1.pack(side='left')
    r2=Radiobutton(fm_2,text='否',variable=v,value=2)
  
    r2.pack(side='right')
   
    bconfirm=Button(fm_3,text="确认")
    bconfirm.pack()
    
    b1=Button(fm_3,text="上一条")
    b1.pack(side='left',anchor='w',padx=40,pady=10)
    b2=Button(fm_3,text="下一条")
    b2.pack(side='right',anchor='e',padx=40,pady=10)
    
    
    
    dswin.mainloop()



#查看上一条评论
def pre_comment(even,text):
    global comment_detail_index
    comment_detail_index-=1
    print(comment_detail_index)
    if comment_detail_index<0:
        comment_detail_index=0
        messagebox.showinfo('提示','已经是第一条评论了')
    #清空text原有内容
    text.delete('1.0','end')
    #读入新的内容
    text.insert('end',comment[comment_detail_index])

#查看下一条评论
def nex_comment(even,text):
    global comment_detail_index
    comment_detail_index+=1
    print(comment_detail_index)
    
    if comment_detail_index>len(comment):
       comment_detail_index=len(comment)-1;
       messagebox.showinfo('提示','已经是最后一条评论了')
    text.delete('1.0','end')
    text.insert('end',comment[comment_detail_index])


    

#批量删除
#不能分开下标使用delete，每次delete后，listbox元素下标会发生变化，不能继续用原来的下标
#可以将要删除的索引从大的开始删除，这样删除后不会影响到较小的索引
def main_delete_multiple():
    tmp=comment_list.curselection()
    index=list(tmp)
    index.sort(reverse=True)
    print(index)
    
    
    for item in index:
        comment_list.delete(item)
    for item in index:
        del comment[item]
    print(comment)
    
    
    #最后将更新后的comment覆盖原来的保存文件
    
#使用3个frame划分布局
#上半部分放text显示评论，下半部分放评论标签,最底放两个按钮
#将text_detail作为参数传入
#问题：只能移动一次，只能看到下一条评论(值传递，无法修改到外部变量)
def comment_detail(even):
    
   
    global comment_detail_index
    #评论内容
    str=comment_list.get(comment_list.curselection())
    tmp=comment_list.curselection()
    print(tmp)
    comment_detail_index=tmp[0]
    print(comment_detail_index)
  
    detail_win=Tk()
    detail_win.geometry("400x400")
    detail_menu=Menu(detail_win)
    detail_menu.add_command(label='添加标签')
    detail_menu.add_command(label='删除标签')
    detail_menu.add_command(label='删除评论')
    detail_win['menu']=detail_menu
    
    fm_text=Frame(detail_win,width=400,height=200,bg='blue')
    fm_tag=Frame(detail_win,width=400,height=150,bg='red')
    fm_button=Frame(detail_win,width=400,height=50,)
    fm_text.grid(row=0)
    fm_tag.grid(row=1)
    fm_button.grid(row=2)
    #显示详细评论
    text_detail=Text(fm_text,width=55,height=14)
    text_detail.pack(side='left')
    #显示标签信息
    
    text_detail.insert("end", str)
    
    tag_sc=Scrollbar(fm_tag)
    tag_sc.pack(side=RIGHT,fill=Y)

    #列表滚动，滚动条跟着滚动
    tag_list=Listbox(fm_tag,width=55,height=10,selectmode=MULTIPLE,yscrollcommand=tag_sc.set)
    tag_list.pack(side=LEFT,fill=BOTH,expand=True)
    #滚动条动，列表跟着滚动
    tag_sc.config(command=tag_list.yview)
    
    
    for item in tag_all:
        tag_list.insert("end",item)
    
   
    
    
    #放置选择上一条和下一条按钮
    #点击按钮后更新评论下标索引，和文本中评论内容
    pre_button=Button(fm_button,text="上一条")
    pre_button.bind("<Button-1>",lambda event:pre_comment(event,text_detail))
    
    nex_button=Button(fm_button,text="下一条")
    nex_button.bind("<Button-1>",lambda event:nex_comment(event,text_detail))
    
    
    pre_button.place(x=0,y=0)
    nex_button.place(x=350,y=0)
    
    detail_win.mainloop()

        
def finished_comment():
    global comment_detail_index
    #评论内容
    
  
    finished_win=Tk()
    finished_win.geometry("400x400")
    finished_menu=Menu(finished_win)
    finished_menu.add_command(label='添加标签')
    finished_menu.add_command(label='删除标签')
    finished_menu.add_command(label='删除评论')
    finished_win['menu']=finished_menu
    
    fm_text=Frame(finished_win,width=400,height=200)
    fm_tag=Frame(finished_win,width=400,height=150)
    fm_button=Frame(finished_win,width=400,height=50,)
    fm_text.grid(row=0)
    fm_tag.grid(row=1)
    fm_button.grid(row=2)
    #显示详细评论
    text_detail=Text(fm_text,width=55,height=14)
    text_detail.pack(side='left')
    #显示标签信息
    
    text_detail.insert("end", str)
    
    label1=Label(fm_tag,text="是否推广贴")
    label1.grid(row=0,column=0)
    v1=IntVar()
    v2=IntVar()
    v1.set(0)
    v2.set(0)
    b1=Radiobutton(fm_tag,text="是",variable=v1,value=1)
    b1.grid(row=0,column=1)
    b2=Radiobutton(fm_tag,text='否',variable=v1,value=2)
    b2.grid(row=0,column=2)
    
    label2=Label(fm_tag,text="评论情感色彩")
    label2.grid(row=1,column=0)
    b3=Radiobutton(fm_tag,text="积极",variable=v2,value=1)
    b3.grid(row=1,column=1)
    b4=Radiobutton(fm_tag,text="中性",variable=v2,value=2)
    b4.grid(row=1,column=2)
    b5=Radiobutton(fm_tag,text="消极",variable=v2,value=3)
    b5.grid(row=1,column=3)
    
    
   
    
    
    #放置选择上一条和下一条按钮
    #点击按钮后更新评论下标索引，和文本中评论内容
    pre_button=Button(fm_button,text="上一条")
    pre_button.bind("<Button-1>",lambda event:pre_comment(event,text_detail))
    
    nex_button=Button(fm_button,text="下一条")
    nex_button.bind("<Button-1>",lambda event:nex_comment(event,text_detail))
    
    
    pre_button.place(x=0,y=0)
    nex_button.place(x=350,y=0)
    
    finished_win.mainloop()
   
    
        
        
    
root=Tk()
root.title("数据标注软件")
root.geometry("800x450")
menubar=Menu(root)

fmenu=Menu(menubar)
fmenu.add_command(label="新建",command=new_file)
fmenu.add_command(label='导入',command=lambda:importfile(comment_list))
fmenu.add_command(label='导出',command=filesaveas)
fmenu.add_command(label='保存',command=filesave)
fmenu.add_command(label='另存为',command=filesaveas)

dmenu=Menu(menubar)
dmenu.add_command(label='下载',command=download)
dmenu.add_command(label='生成统计图',command=datachart)

dmenu.add_command(label='添加标注')
dmenu.add_command(label='删除评论',command=main_delete_multiple)
dmenu.add_command(label='已标注评论',command=finished_comment)
dmenu.add_command(label='未标注评论',command=finished_comment)


menubar.add_cascade(label='文件',menu=fmenu)
menubar.add_cascade(label='数据',menu=dmenu)
menubar.add_command(label='标签',command=tag)

root['menu']=menubar

#主界面 listbox+滚动条，显示股票评论，listbox设置为多选
#双击一条评论，弹出新的窗口comment_detail查看评论的详细信息

#设置滚动条
sc=Scrollbar(root)
sc.pack(side=RIGHT,fill=Y)

#列表滚动，滚动条跟着滚动
comment_list=Listbox(root,width=100,height=15,selectmode=MULTIPLE,yscrollcommand=sc.set)
comment_list.pack(side=LEFT,fill=BOTH,expand=True)

#滚动条动，列表跟着滚动
sc.config(command=comment_list.yview)

#双击显示评论
comment_list.bind("<Double-Button-1>",comment_detail)


#添加评论到listbox中
for item in comment:
    comment_list.insert("end",item)


    
root.mainloop()