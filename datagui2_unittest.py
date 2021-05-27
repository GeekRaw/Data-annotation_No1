# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:57:28 2021

@author: byzjz
"""

import unittest
from datagui2_test import*
from tkinter import*
from tkinter import ttk
from tkinter.messagebox import askokcancel,showinfo,WARNING
import ast
import json
import os
import copy

class stock:
    def __init__(self):
        self.comment_text=''
        self.label_list=[]
        self.tag=0
        
class intvar:
    def __init__(self):
        self.num=0
    def set(self,count):
        self.num=count
    def get(self):
        return self.num

class data_test(unittest.TestCase):
    
    #测试labeled_comment_saveas,判断是否正确导出评论数据
    #给定一组测试数据,写入到文件中，再打开文件读取数据，判断写入和读取数据是否相同
    #导出数据后，要将评论数据的标志为全部置0，判断是否全部置0
    def test_labeled_comment_saveas(self):
        labeled_comment=[]
        labeled_comment_test=[]
        check_dict={}
        check_dict['comment_text']="一直跌不涨，心理压力挺大的"
        check_dict['label_list']=[{"tag":"是否推广","是":1,"否":2,"choice":2}]
        #labeled_comment存储的是stock结构体
        tmp=stock()
        tmp.comment_text=check_dict['comment_text']
        tmp.label_list=check_dict['label_list']
        tmp.tag=1
        labeled_comment.append(tmp)
        labeled_comment_test.append(copy.deepcopy(tmp))
        
        labeled_comment_read=[]
        
        
        f=labeled_comment_saveas(labeled_comment)
        fh=open(f,'r')
        for line in fh.readlines():
            dic=ast.literal_eval(line)
            s_tmp=stock()
            s_tmp.comment_text=dic['comment_text']
            s_tmp.label_list=dic['label_list']
            s_tmp.tag=dic['tag']
            labeled_comment_read.append(s_tmp)
        fh.close()
         
        tag_count=0
        f_comment=open('xueqiu_comment.json','r')
        for line in f_comment.readlines():
            comment_dict=ast.literal_eval(line)
            if comment_dict['tag']==1:
                tag_count+=1
                
        f_comment.close()
        
        self.assertEquals(labeled_comment_test[0].comment_text,labeled_comment_read[0].comment_text,'导出数据错误')
        self.assertEqual(tag_count,0,'重置标志位错误')
        
        
            
     
    
    #测试statistics_saveas,statistics_saveas导出统计图数据，并且将统计图中的选项清0
    #给定一组测试数据，写入到文件中，再打开文件读取数据，判断写入和读取的数据是否相同
    #读出统计图文件中的数据判断选项是否清0
    def test_statistics_saveas(self):
        data_list=[]
        statistics_dict={"tag":"是否推广贴","是":2,"否":10}
        data_list.append(statistics_dict)
        data_list1=[]
        data_list1.append(copy.deepcopy(statistics_dict))
        
        f=statistics_saveas(data_list)
        
      
        
        data_list_test=[]
        fh=open(f,'r')
        for line in fh.readlines():
            dic=json.loads(line)
            data_list_test.append(dic)
        fh.close()
        
        test_count=0
        for item in data_list:
            for key in item:
                if key!='tag':
                    if item[key]!=0:
                        test_count+=1
        
        self.assertEquals(data_list1,data_list_test,'导出数据出错')
        self.assertEquals(test_count,0,'导出数据出错')
        
    
    #测试check_diff用于保存导入的文件数据中选项不同的数据
    #使用两组测试数据，判断check_diff是否能正确找出其中不同的值
    def test_check_diff(self):
        check_dict1={}
        check_dict1['comment_text']="一直跌不涨，心理压力挺大的"
        check_dict1['label_list']=[{"tag":"是否推广","是":1,"否":2,"choice":2}]
        
        check_dict2={}
        check_dict2['comment_text']="一直跌不涨，心理压力挺大的"
        check_dict2['label_list']=[{"tag":"是否推广","是":1,"否":2,"choice":1}]
        
        test_check_list1=[]
        test_check_list1.append(check_dict1)
        
        test_check_list2=[]
        test_check_list2.append(check_dict2)
        
        
        test_check_list=[]
        test_check_list.append(test_check_list1)
        test_check_list.append(test_check_list2)
        
        diff_index=[]
        
        check_test_ans=[]
        check_test_ans.append(0)
        
        check_comment_list=Text()
        
        check_tmp_index=check_diff(test_check_list,diff_index,check_comment_list)
        
        self.assertEquals(check_test_ans,check_tmp_index,'核查成功')
        
        
        
    
    #check_choice_select保存对选项的修改
    #测试是否正确保存修改后的值
    #测试数据设置要修改的值v
    #通过函数check_choice_select将修改后的值保存到对应的数据结构中
    #最后通过判断v与数据结构中对应的值是否相同
    def test_check_choice_select(self):
        #测试数据
        check_dict={}
        check_dict['comment_text']="一直跌不涨，心理压力挺大的"
        check_dict['label_list']=[{"tag":"是否推广","是":1,"否":2,"choice":2}]
        
        #使用两层list
        check_list=[]
        check_list.append(copy.deepcopy(check_dict))
        check_list1=[]
        check_list1.append(check_list)
        
        v=intvar()
        v.set(1)
       
        index=0
        curr_diff_index=[]
        curr_diff_index.append(0)
        diff_index=[]
        diff_index.append(0)
        
        ans=check_choice_selet(v,index,curr_diff_index,diff_index,check_list1)
        self.assertEquals(ans,v.get(),'修改选项错误')
        
    
    
    #判断核查后的数据是否正确导出
    #先将测试数据写入一个list中，然后通过check_saveas函数写入指定的文件中
    #再打开这个指定的文件，将里面的数据读入到另一个list中
    #最后判断这两个list是否相等
    
    def test_check_saveas(self):
        
        
        check_comment_list=Listbox()
        check_dict={}
        check_dict['comment_text']="一直跌不涨，心理压力挺大的"
        check_dict['label_list']=[{"tag":"是否推广","是":1,"否":2,"choice":2}]
        
        #使用两层list
        check_list=[]
        check_list.append(copy.deepcopy(check_dict))
        check_list1=[]
        check_list1.append(check_list)
        
        #check_list1在check_saveas函数中会被清空，再深拷贝一份
        check_list2=[]
        check_list2.append(copy.deepcopy(check_list))
      
        f=check_saveas(check_list1,check_comment_list)
        
        check_list_tmp=[]
        f=open(f,"r")
        for line in f.readlines():
            dic=json.loads(line)
            check_list_tmp.append(dic)
        f.close()
      
        
        self.assertEquals(check_list2[0], check_list_tmp,'写入数据错误')
        
        
        


if __name__=='__main__':
    unittest.main(verbosity=2)
        