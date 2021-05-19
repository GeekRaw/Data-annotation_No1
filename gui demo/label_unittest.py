# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:49:33 2021

@author: byzjz
"""
'''
unitest case的运行流程:
写好一个完整的TestCase
多个TestCase由TestLoader被加载都TestSuite中，TestSuite可以嵌套TestSuite
由TextRuner来执行TestSuite，测试结果保存在TextTestResult中
TestFixtur指的是环境准备和恢复

TestFixture用于环境的准备和恢复，一般使用到下面的函数：
setUp():准备环境，执行每个测试用例的前置条件
tearDown():环境还原，执行每个测试用例的后置条件
setUpClass():必须使用@classmethod装饰器，所有case执行的前置条件，只运行一次
tearDownClass():必须使用@classmethod装饰器，所有case运行后只运行一次


'''

import unittest
import logging

from datagui_test import*
from tkinter import*
from tkinter import ttk



class label_test(unittest.TestCase):
   
        
    
    #测试添加标签名
    #测试数据指定标签名，判断写入的标签名是否与指定的标签名相同
    def test_label_name_test(self):
        en=Entry()
        en.insert(0, '是否推广贴')
        s=en.get()
        tag_tmp={}
        data_label={}
        res1,res2=tag_name_confirm(en,tag_tmp,data_label)
        print(res1)
        print(res2)
        self.assertEqual(s, res1,'添加标签名错误')
        self.assertEqual(s, res2,'添加标签名错误')
        
    #测试是否正确删除标签选项
    #测试数据指定删除的标签选项，判断删除的标签名是否与指定的标签名相同
    
    def test_label_choice_delete(self):
        choice=Listbox()
        choice.insert('end', '消极')
        choice.select_set(0)
        tag_tmp={'消极':'消极'}
        event='<Button-3>'
        s1,s2=choice_delete(event,choice,tag_tmp)
        self.assertEqual(s1, s2)
    
    #测试是否正确添加选项
    #选项是否写入到数据结构中
    #选项是否写入到显示的listbox中
    #测试数据指定添加的选项，判断数据结构和listbox中添加的选项是否与指定的选项相同
    def test_label_choice(self):
        event='<Button-1>'
        input_choice=Entry()
        input_choice.insert(0,'积极')
        choice_list=Listbox()
        choice_index=[]
        choice_index.append(1)
        tag_tmp={}
        data_label={}
        dict1,dict2,index=tag_choice_confirm(input_choice,choice_list,tag_tmp,data_label,choice_index)
       
        (k1,v1),=dict1.items()
        (k2,v2),=dict2.items()
        self.assertEqual(k1,k2)
        self.assertEqual(v1+1,index)
        self.assertEqual(v2,0)
        
        
    
    #测试写入到文件中的标签信息是否正确
    #tag_tmp是标签类中的标签项
    #data_label是统计图中的标签统计项
    #测试指定写入的标签项，通过判断写入标签类和统计图的信息是否与指定的标签相同来判断是否正确写入标签信息
    
    def test_create(self):
        event='<Button-1>'
        tag_tmp={'tag':'是否推广贴','是':1,'否':2,'choice':0}
        data_label={}
        new_label={'tag':'是否推广贴','是':0,'否':0}
        tag_all=[]
        tag_listbox=Listbox()
       
        
        
        dict1,dict2=create_confirm(event,tag_tmp,new_label,data_label,tag_all,tag_listbox)
        
        
        self.assertEqual(dict1,tag_tmp)
        self.assertEqual(dict2[0]['tag'],new_label['tag'])
        
        
    
    #在标签管理类中删除标签
    #测试是否正确删除指定的标签
    #测试数据指定删除的标签，通过判断返回删除的标签是否与指定的标签相同来判断是否正确删除
    def test_label_delete(self):
        #显示界面中的标签
        tag_list=Listbox()
        tag_list.insert('end','是否推广贴')
        tag_list.select_set(0)
        
        tag_all=[]
        tag_all.append('是否推广贴')
        tag_tmp=[]
        tag_tmp.append('是否推广贴')
        delete_list=tag_delete(tag_list,tag_all)
        self.assertEqual(tag_tmp[0],delete_list[0],'删除错误')
        
        
   


if __name__=='__main__':
    unittest.main(verbosity=2)