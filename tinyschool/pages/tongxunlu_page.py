from selenium.webdriver.common.by import By
from time import sleep
from pages.login_page import Login_Page
from workbog.ranzhi_fun import RanZhi_Fun


class TongXunLu_Page(Login_Page):
    def tongxunlu_page(self,username):
        driver = self.driver
        read = self.ready['TongXunLu_Page']
        sleep(3)
        # 点击通讯录
        driver.click(read['DONGXUNLU'])
        sleep(2)
        # 清空搜索框
        driver.clear(read['SOUSUO'])
        sleep(3)
        # 输入搜索的学生姓名
        driver.input(read['SOUSUO'],username)
        sleep(3)
        # 点击搜索
        driver.click(read['DIANSOUSUO'])


    def tongxunlusuccess_assert(self):
        sleep(3)
        read = self.ready['TongXunLu_Page']
        # self.driver.show_wait((By.LINK_TEXT, self.read['SHOWWAIT']))
        return self.driver.get_text(read['STUDENTNAME'])
        # a = driver.get_text(read['STUDENTNAME'])
        print(type(a))



if __name__ == '__main__':
    driver = RanZhi_Fun('Chrome')
    b = TongXunLu_Page(driver)
    b.loginpage("http://0855.91vschool.cn/#/index","13450953452","qtjy123456")
    b.tongxunlu_page("测试01")
    b.tongxunlusuccess_assert()

