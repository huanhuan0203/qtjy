from selenium import webdriver
# 下拉框
from selenium.webdriver.support.select import Select
# 鼠标事件
from selenium. webdriver.common.action_chains import ActionChains
# 键盘时间
from selenium. webdriver. common.keys import Keys
# 显示等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 时间包
from time import sleep
import openpyxl
import csv
import yaml

import logging
import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class RanZhi_Fun():
    '''常用的web项目方法'''

    def __init__(self, browser_type):
        '''
        定义浏览器的类型
        :param browser_type: 指定打开浏览器的类型,比如"Chrome","Firefox"
        '''
        if browser_type == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser_type == "Firefox":
            self.driver = webdriver.Firefox()
        elif browser_type == "Ie":
            self.driver = webdriver.Ie()
        self.driver.maximize_window()

    def open(self, url):
        '''
        打开指定的网址
        :param url: 输入要打开网址的url
        '''
        self.driver.get(url)

    def find_ele(self, selectors):
        '''
        定位一个元素,你可有八种方法去实现
        :param selectors: 传入定位的方法和值,格式为:'方法,值'
        :return: 返回定位到的元素
        '''
        ele_type = selectors.split(',')[0].strip()
        ele_value = selectors.split(',')[1].strip()
        if ele_type == "id" or ele_type == "i":
            ele = self.driver.find_element_by_id(ele_value)
        elif ele_type == "name" or ele_type == "n":
            ele = self.driver.find_element_by_name(ele_value)
        elif ele_type == "class" or ele_type == "c":
            ele = self.driver.find_element_by_class_name(ele_value)
        elif ele_type == "tag" or ele_type == "t":
            ele = self.driver.find_element_by_tag_name(ele_value)
        elif ele_type == "link" or ele_type == "l":
            ele = self.driver.find_element_by_link_text(ele_value)
        elif ele_type == "partial" or ele_type == "p":
            ele = self.driver.find_element_by_partial_link_text(ele_value)
        elif ele_type == "xpath" or ele_type == "x":
            ele = self.driver.find_element_by_xpath(ele_value)
        elif ele_type == "css" or ele_type == "s":
            ele = self.driver.find_element_by_css_selector(ele_value)
        return ele

    def find_eles(self, selectors):
        '''
        定位一组元素,你可有八种方法去实现
        :param selectors: 传入定位的方法和值,格式为:'方法,值'
        :return: 返回定位到的一组元素,格式是以列表的形式返回
        '''
        ele_type = selectors.split(',')[0].strip()
        ele_value = selectors.split(',')[1].strip()
        if ele_type == "id" or ele_type == "i":
            eles = self.driver.find_elements_by_id(ele_value)
        elif ele_type == "name" or ele_type == "n":
            eles = self.driver.find_elements_by_name(ele_value)
        elif ele_type == "class" or ele_type == "c":
            eles = self.driver.find_elements_by_class_name(ele_value)
        elif ele_type == "tag" or ele_type == "t":
            eles = self.driver.find_elements_by_tag_name(ele_value)
        elif ele_type == "link" or ele_type == "l":
            eles = self.driver.find_elements_by_link_text(ele_value)
        elif ele_type == "partial" or ele_type == "p":
            eles = self.driver.find_elements_by_partial_link_text(ele_value)
        elif ele_type == "xpath" or ele_type == "x":
            eles = self.driver.find_elements_by_xpath(ele_value)
        elif ele_type == "css" or ele_type == "s":
            eles = self.driver.find_elements_by_css_selector(ele_value)
        return eles

    def input(self, selectors, value):
        '''
        向定位到的元素输入一定的内容
        :param selectors: 传入定位的方法和值,格式为:'方法,值'
        :param value: 自己想输入的内容
        :return:
        '''
        self.find_ele(selectors).send_keys(value)

    def click(self, selectors):
        '''
        点击页面定位到的元素
        :param selectors: 传入定位的方法和值,格式为:'方法,值'
        :return:
        '''
        self.find_ele(selectors).click()

    def get_text(self, selectors):
        '''
        获取定位到元素的文本值
        :param selectors: 传入定位的方法和值,格式为:'方法,值'
        :return: 返回获取到的文本值
        '''
        text = self.find_ele(selectors).text
        return text

    def switch_window(self,value):
        '''
        切换窗口
        :param value: 
        :return: 
        '''
        hand = self.driver.window_handles[value]
        self.driver.switch_to.window(hand)

    def clear(self, selectors):
        '''
        清除输入框
        :param selectors: 传入定位的方法和值,格式为:'方法,值'
        :return: 
        '''
        self.find_ele(selectors).clear()

    def switch_frame(self,selectors):
        '''
        嵌套层
        :param selectors: 传入定位的方法和值,格式为:'方法,值'
        :return: 
        '''
        ifm = self.find_ele(selectors)
        self.driver.switch_to.frame(ifm)

    def swich_up_frame(self):
        '''
        返回上一层嵌套
        :return: 
        '''
        self.driver.switch_to.parent_frame()

    def swich_finally_frame(self):
        '''
        返回到最外层嵌套
        :return: 
        '''
        self.driver.switch_to.default_content()

    def select_downbox(self,selectors,values):
        '''
        下拉框
        :param selectors: 传入定位的方法和值,格式为:'方法,值'
        :param values: 下拉框的类型和值
        :return: 
        '''
        se = self.find_ele(selectors)
        ele_type = values.split(',')[0].strip()
        ele_value = values.split(',')[1].strip()
        if ele_type == "text" or ele_type == "t":
            Select(se).select_by_visible_text(ele_value)
        elif ele_type == "index" or ele_type == "i":
            Select(se).select_by_index(int(ele_value))
        elif ele_type == "value" or ele_type == "v":
            Select(se).select_by_value(ele_value)

    def mouse_event(self,selectors,type):
        '''
        鼠标事件
        :return: 
        '''
        right = self.find_ele(selectors)
        # 鼠标右键事件
        if type == "context_click" or type == "cc":
            ActionChains(self.driver).context_click(right).perform()
            #鼠标双击事件
        elif type == "double_click" or type == "dc":
            ActionChains(self.driver).double_click(right).perform()
            #鼠标悬停操作
        elif type == "move_to_element" or type == "mte":
            ActionChains(self.driver).move_to_element(right).perform()
            #鼠标单击操作
        elif type == "click" or type == "c":
            ActionChains(self.driver).click(right).perform()

    def key_event(self,selectors,kw,cv = ''):
        '''
        键盘事件
        :param selectors: 
        :param kw: 
        :param cv: 
        :return: 
        '''
        key = self.find_ele(selectors)
        # 回车
        if kw == "ENTER" or kw == "E":
            key.send_keys(Keys.ENTER)
            # 换行
        elif kw == "TAB" or kw == "T":
            key.send_keys(Keys.TAB)
            # 方向键下
        elif kw == "DOWN" or kw == "D":
            key.send_keys(Keys.DOWN)
            # 方向键上
        elif kw == "UP" or kw == "U":
            key.send_keys(Keys.UP)
            # 方向键左
        elif kw == "LEFT" or kw == "L":
            key.send_keys(Keys.LEFT)
            # 方向键右
        elif kw == "RIGHT" or kw == "R":
            key.send_keys(Keys.RIGHT)
            # 键盘空格
        elif kw == "SPACE" or kw == "S":
            key.send_keys(Keys.SPACE)
            # 键盘回退键
        elif kw == "BACKSPACE" or kw == "B":
            key.send_keys(Keys.BACKSPACE)
            # 特殊操作，复制，全选，粘贴，剪切
        elif kw == "CONTROL" or kw == "C":
            key.send_keys(Keys.CONTROL,cv)

    def show_wait(self,selectors):
        '''

        :param selectors:
        :return:
        '''
        WebDriverWait(self.driver,100).until(EC.presence_of_all_elements_located(selectors))

    #  关闭浏览器
    def close(self):
        self.driver.quit()

    def get_screenshot(self,filepath):
        self.driver.get_screenshot_as_file(filepath)

    def hide_wait(self,time):
        '''
        隐式等待
        :param time: 
        :return: 
        '''
        self.driver.implicitly_wait(time)

    def roll_line(self,selectors):
        '''
        滚动条
        :return: 
        '''
        ele_znxf = self.find_ele(selectors)
        JS ='arguments[0].scrollIntoView()'
        self.driver.execute_script(ele_znxf)

class Open_Cx():
    def open_csv(self,url):
        '''
        读取csv文件的方法
        :param url: csv的路径
        :return: 返回列表
        '''
        with open(url,encoding='utf8') as csv_file:
            get_csv = csv.reader(csv_file)
            get_csv_data = []
            skip = True
            for i in get_csv:
                if skip:
                    skip = False
                    continue
                get_csv_data.append(tuple(i))
            return get_csv_data

    def open_xlsx(self,url,forname):
        '''
        读取xlsx文件的方法
        :param url: xlsx的路径
        :param forname: xlsx的单元格
        :return: 
        '''
        we = openpyxl.load_workbook(url)
        get_excel = we[forname]
        excle_data = []
        skip = True
        for i in get_excel:
            if skip:
                skip = False
                continue
            excle_data1 = []
            for j in i:
                if j.value == None:
                    j.value = ""
                excle_data1.append(j.value)
            excle_data.append(tuple(excle_data1))
        return excle_data

class PublicPage():
    def __init__(self,driver:RanZhi_Fun):
        self.driver = driver

class ReadYaml():
    def readyaml(self,url):
        with open(url,encoding='utf8') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
            return yaml_data

class SendLog:
    def __init__(self, log_path):
        self.file_name = log_path
        self.logger = logging.getLogger()
        # 设置日志的级别
        self.logger.setLevel(logging.DEBUG)
        # 设置日志的格式与内容
        self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-[%(levelname)s]:%(message)s')

    def _console(self, level, message):
        # 创建一个FileHandler对象，把日志内容追加到末尾
        fh = logging.FileHandler(self.file_name,'a','utf8')
        fh.setLevel(logging.DEBUG)
        # 设置文件内容的格式
        fh.setFormatter(self.formatter)
        # 将内容添加到日志文件
        self.logger.addHandler(fh)

        # 创建StreamHandler对象，把日志输出到控制台
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 避免日志输出重复
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        fh.close()

    def info(self, message):
        self._console('info', message)

    def debug(self, message):
        self._console('debug', message)

    def warning(self, message):
        self._console('warning', message)

    def error(self, message):
        self._console('error', message)
class SendEmail:

    def sendemail(self, report_path,sender,pwd,receiver,subject):
        '''配置邮件服务器信息'''
        # 配置163邮箱
        smtpserver = 'smtp.163.com'
        port = 25
        # 配置QQ邮箱
        # smtpserver = 'smtp.qq.com'
        # port = 465

        # 创建邮件对象
        msg = MIMEMultipart()
        # 发送人、收件人、邮件的主题
        msg['from'] = sender
        # 有多个收件人时，以分好隔开
        msg['to'] = ';'.join(receiver)
        msg['subject'] = subject

        # 读取测试报告内容
        with open(report_path, 'rb') as rf:
            body = rf.read()

        # 写邮件的正文
        mine_text = MIMEText(body,'html','utf8')
        msg.attach(mine_text)

        # 写附件内容
        att = MIMEText(body,'base64','utf8')
        att['Content-type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename="%s"' % report_path
        msg.attach(att)

        # 发送邮件
        # 用163发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver,port)
        smtp.login(sender,pwd)
        smtp.sendmail(sender,receiver.split(';'),msg.as_string())
        smtp.close()
        print('发送邮件成功！')

        # 用QQ发送邮件
        # smtp = smtplib.SMTP_SSL(smtpserver, port)
        # smtp.connect(smtpserver,port)
        # smtp.login(sender,pwd)
        # smtp.sendmail(sender,receiver.split(';'),msg.as_string())
        # smtp.close()
        # print('发送邮件成功！')



class GetPath:
    def get_path(self,file_path):
        full_path = os.path.dirname(__file__)
        project_name = file_path.split('\\')[0]
        parent_path = full_path.split(project_name)[0]
        return parent_path + file_path






        
        







