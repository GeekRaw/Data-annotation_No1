# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:34:28 2021

@author: byzjz
"""

import unittest
import copy
from datagui_test import*
from tkinter import*
from tkinter import ttk


class stock:
    def __init__(self):
        self.comment_text=''
        self.label_list=[]
        self.tag=0
        
class  data_test(unittest.TestCase):
    
     #测试单选按钮是否正常选择
     #先设置按钮选择的值，然后返回按钮选择后的值，通过判断两个值是否相等来判断单选按钮是否正常工作
    def test_radiobutton_select(self):
         v=IntVar()
         v.set(1)
         unlabeled_comment_list=[]
         unlabeled_index=[]
         unlabeled_index.append(0)
         tmp=stock()
         tmp.comment_text='中国平安(SH601318)什么情况'
         label_tmp={'tag':'是否推广贴','是':1,'否':2,'choice':0}
         tmp.label_list.append(label_tmp)
         index=0
         unlabeled_comment_list.append(tmp)
         ans=select(v,index,unlabeled_index,unlabeled_comment_list)
         self.assertEqual(ans,v.get(),'单选按钮选择出错')
    
    #测试未标注评论中上一条按钮是否正常工作
    #给定测试数据，通过判断执行上一条操作后返回的评论是否与测试数据相同来判断是否上一条是否正常工作
     
    def test_unlabeled_pre_comment(self):
        fm_choice=Frame()
        unlabeled_index=[]
        unlabeled_index.append(1)
        unlabeled_comment_list=[]
        tmp=stock()
        tmp.comment_text='中国平安(SH601318)什么情况'
        label_tmp={'tag':'是否推广贴','是':1,'否':2,'choice':0}
       
        tmp.label_list.append(label_tmp)
        unlabeled_comment_list.append(tmp)
        
        tmp2=stock()
        tmp2.comment_text='我感觉中国平安也是破位走势了'
        label_tmp={'tag':'是否推广贴','是':1,'否':2,'choice':0}
        tmp2.label_list.append(label_tmp)
        unlabeled_comment_list.append(tmp2)
        
        text=Text()
        #Text控件中插入第2条评论
        text.insert('end','我感觉中国平安也是破位走势了')
        ans=pre_unlabeled_comment(fm_choice,unlabeled_index,unlabeled_comment_list,text)
        self.assertEqual(ans, unlabeled_comment_list[0].comment_text,'上一条功能出错')
       
        
    #测试未标注评论中下一条按钮是否正常工作
    #给定测试数据，通过判断执行下一条操作后返回的评论信息是否与测试数据相同来判断下一条功能是否正常工作
    def test_unlabeled_nxt_comment(self):
        fm_choice=Frame()
        unlabeled_index=[]
        unlabeled_index.append(0)
        unlabeled_comment_list=[]
        tmp=stock()
        tmp.comment_text='中国平安(SH601318)什么情况'
        label_tmp={'tag':'是否推广贴','是':1,'否':2,'choice':0}
       
        tmp.label_list.append(label_tmp)
        unlabeled_comment_list.append(tmp)
        
        tmp2=stock()
        tmp2.comment_text='我感觉中国平安也是破位走势了'
        label_tmp={'tag':'是否推广贴','是':1,'否':2,'choice':0}
        tmp2.label_list.append(label_tmp)
        unlabeled_comment_list.append(tmp2)
        
        text=Text()
        #Text控件中插入第一条评论
        text.insert('end','中国平安(SH601318)什么情况')
        ans=nxt_unlabeled_comment(fm_choice,unlabeled_index,unlabeled_comment_list,text)
        self.assertEqual(ans, unlabeled_comment_list[1].comment_text,'下一条功能出错')
        
     #测试已标注评论的上一条按钮是否正常工作
     #点击上一条按钮后，评论信息和选项的选择信息是分开更新的
     #给定测试数据，判断评论信息和选项的选择信息是否在执行上一条操作后与测试数据相同
    def test_labeled_comment_pre(self):
            fm_choice=Frame()
            labeled_index=[]
            labeled_index.append(1)
            labeled_comment_list=[]
            tmp=stock()
            tmp.comment_text='中国平安(SH601318)什么情况'
            label_tmp={'tag':'是否推广贴','是':1,'否':2,'choice':1}
       
            tmp.label_list.append(label_tmp)
            labeled_comment_list.append(tmp)
        
            tmp2=stock()
            tmp2.comment_text='我感觉中国平安也是破位走势了'
            label_tmp={'tag':'是否推广贴','是':1,'否':2,'choice':2}
            tmp2.label_list.append(label_tmp)
            labeled_comment_list.append(tmp2)
        
            text_test=Text()
            #Text控件中插入第2条评论
            text_test.insert('end','我感觉中国平安也是破位走势了')
            old_labeled_choice=[]
            
            comment,choice_list=labeled_pre_comment(fm_choice,labeled_index,labeled_comment_list,text_test,old_labeled_choice)
            self.assertEqual(labeled_comment_list[0].comment_text,comment,'评论信息显示错误')
            self.assertEqual(labeled_comment_list[0].label_list[0]['choice'],choice_list[0]['old_choice'],'选项信息显示错误')
            
            
        
        #测试已标注数据的下一条按钮是否正常工作
        #点击下一条按钮后，评论信息和选项的选择信息是分开更新的
        #给定测试数据，判断评论信息和选项的选择信息是否在执行下一条操作后与测试数据相同
    def test_labeled_comment_nxt(self):
            fm_choice=Frame()
            labeled_index=[]
            labeled_index.append(0)
            labeled_comment_list=[]
            tmp=stock()
            tmp.comment_text='中国平安(SH601318)什么情况'
            label_tmp={'tag':'是否推广贴','是':1,'否':2,'choice':1}
       
            tmp.label_list.append(label_tmp)
            labeled_comment_list.append(tmp)
        
            tmp2=stock()
            tmp2.comment_text='我感觉中国平安也是破位走势了'
            label_tmp={'tag':'是否推广贴','是':1,'否':2,'choice':2}
            tmp2.label_list.append(label_tmp)
            labeled_comment_list.append(tmp2)
        
            text_test=Text()
            #Text控件中插入第1条评论
            text_test.insert('end','中国平安(SH601318)什么情况')
            old_labeled_choice=[]
            
            comment,choice_list=labeled_nxt_comment(fm_choice,labeled_index,labeled_comment_list,text_test,old_labeled_choice)
            self.assertEqual(labeled_comment_list[1].comment_text,comment,'评论信息显示错误')
            self.assertEqual(labeled_comment_list[1].label_list[0]['choice'],choice_list[0]['old_choice'],'选项信息显示错误')
    
    #测试已标注评论的选项选择功能
    #先设置按钮选择的值,然后返回按钮选择后的值，通过判断是否相等来判断是否正常工作
    #因为是已经标注的评论,需要保存原来的值和新选择的值，以便更新文件中的数据
    #使用old_labeled_choice保存新旧选项，测试old_labeled_choice是否正确更新
    def test_labeled_select(self):
        v=IntVar()
        
        v.set(2)
        index=0
        label_index=[]
        label_index.append(0)
        labeled_comment_list=[]
        tmp=stock()
        tmp.comment_text='中国平安(SH601318)什么情况'
        label_tmp={'tag':'是否推广贴','是':1,'否':2,'choice':1}
        
        old_labeled_choice=[]
        tmp2={'tag':'是否推广贴'}
        old_labeled_choice.append(tmp2)
       
        tmp.label_list.append(label_tmp)
        labeled_comment_list.append(tmp)
        choice_selected,choice_list=labeled_select(v,index,label_index,labeled_comment_list,old_labeled_choice)
        self.assertEqual(v.get(),choice_selected,'选项选择出错')
        self.assertEqual(v.get(),choice_list[0]['new_choice'],'选项更新出错')
    
    #测试更改已标注评论的选项
    #更改已标注评论数据的选择后，统计图中对应的选项数据也要更改
    #old_labeled_choice保存了旧的选择数据(old_choice)和新的选择数据(new_choice),用来更新统计图数据
    #通过传入统计图选项选择的测试数据，在经过更改选项选择后，判断数据的增减是否与测试数据相同
    def test_labeled_change(self):
        event='<Button-1>'
        labeled_index=[]
        labeled_index.append(0)
        labeled_comment_list=[]
        data_list=[]
        tmp_data={'tag':'是否推广贴','是':10,'否':20}
        tmp_data2={'tag':'是否推广贴','是':10,'否':20}
        data_list.append(tmp_data)
        
        old_labeled_choice=[]
        tmp_old={'tag':'是否推广贴','old_choice':1,'new_choice':2}
        
        list_data=labeled_change_confirm(event,labeled_index,labeled_comment_list,data_list,old_labeled_choice)
        self.assertEqual(tmp_data2['是'],list_data[0]['是'],'更新统计图数据错误')
        self.assertEqual(tmp_data2['否'],list_data[0]['否'],'更新统计图数据错误')
    
        
    
            
        
if __name__=='__main__':
    unittest.main(verbosity=2)
        
        
        