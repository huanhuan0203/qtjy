from selenium.webdriver.common.by import By
from time import sleep
from pages.login_page import Login_Page
from workbog.ranzhi_fun import RanZhi_Fun


class AddStudent_Page(Login_Page):
    def addstudent_page(self):
        driver = self.driver
        read = self.ready['AddStudent_Page']
        sleep(3)
        # 点击通讯录
        driver.click(read['DONGXUNLU1'])
        # 点击新增人员
        sleep(2)
        driver.click(read['ADDREN'])
        # 点击新增学生
        sleep(2)
        driver.click(read['ADDSTUDENT'])
        # 选择班级
        sleep(2)
        driver.click(read['BANJI'])
        # 选择具体的班级
        sleep(2)
        driver.click(read['BANJI1'])
        # 再次点击确定班级
        sleep(1)
        driver.click(read['BANJI'])
        # 学生姓名
        sleep(1)
        driver.input(read['STUDENTNAME'],'测试')
        # 学生身份证号
        driver.input(read['STUDENTHAO'],'110101199003073415')
        # 学生联系电话
        sleep(1)
        driver.input(read['STUDENTDIAN'],'18256478965')
        # 家长姓名
        sleep(1)
        driver.input(read['JIANAME'],'测试')
        # 联系电话
        sleep(1)
        driver.input(read['DIANHUA'],'18266996633')
        # 家长身份证号
        sleep(1)
        driver.input(read['JIAHAO'],'110101199003072930')
        #  亲属关系
        sleep(1)
        driver.click(read['GUANXI'])
        #  具体的亲属关系
        sleep(1)
        driver.click(read['GUANXI1'])
        #  保存
        sleep(1)
        driver.click(read['STUDENTBAOCEN'])


if __name__ == '__main__':
    driver = RanZhi_Fun('Chrome')
    b = AddStudent_Page(driver)
    b.loginpage("http://0855.91vschool.cn/#/index","13450953452","qtjy123456")
    b.addstudent_page()