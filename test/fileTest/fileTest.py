# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:44:54 2021

@author: lijia
"""

"""
准备测试环境
"""
try:
    import os
    import json
    import logging
    #设置日志格式
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
except:
    print("请配置好logging环境，以便于正常输出log日志")

try:
    import unittest
    logging.info("unitest库成功导入")
except:
    logging.warning("请配置好unittest测试环境！")

try:
    from tkinter import *
    from tkinter import ttk
    from tkinter.filedialog import*
    import tkinter
    from tkinter.messagebox import askokcancel,showinfo,WARNING
    import ast
    logging.info("tkinter、ast库成功导入")
except:
    logging.warning("请配置好tkinter、ast环境！")
    
# 文件功能测试类
class fileTest(unittest.TestCase):
    def setUp(self):
        #测试前需执行的操作
        self.jsonFile = "test.json"
        self.txtFile = "test.txt"
        with open(self.jsonFile,"w") as f:
            json.dump({'comment_text': '中国平安(SH601318)太惨了上海机场(SH600009)'}, f)
            logging.info("成功创建json文件")
        with open(self.txtFile, "w") as f:
            logging.info("成功创建txt文件")
    
    def tearDown(self):
        #测试用例执行完后所需执行的操作
        if os.path.exists(self.jsonFile):
            os.remove(self.jsonFile)
            logging.info("成功删除json文件")
        else:
            logging.warning("没有找到json文件！")
            
        if os.path.exists(self.txtFile):
            os.remove(self.txtFile)
            logging.info("成功删除txt文件")
        else:
            logging.warning("没有找到txt文件！")

    def testImportFile(self):   #  导入json文件功能测试
        #具体的测试脚本
        name = importfile(Listbox()).split('/')[-1]
        self.assertEqual(self.jsonFile[-4:], name[-4:], "导入文件失败")

    def testNewFile(self):  # 新建文件功能测试
        try:
            new_file()
            logging.info("新建文件功能正常！")
        except:
            logging.warning("新建文件功能出现错误！")
            
    def testSaveFile(self): # 导出文件功能测试
        try:
            filesave()   
            logging.info("导出文件功能正常！")
        except:
            logging.warning("导出文件功能出现错误！")
    
    def testSaveAsFile(self): # 文件另存功能测试
        try:
            filesaveas() 
            logging.info("文件另存功能正常！")
        except:
            logging.warning("文件另存功能出现错误！")         
    
        
        
if __name__ == "__main__":
    try:
        from datagui import importfile, new_file, filesave, filesaveas
        logging.info("测试代码成功导入")
    except:
        logging.warning("测试代码未成功导入，请检查！")
    unittest.main()