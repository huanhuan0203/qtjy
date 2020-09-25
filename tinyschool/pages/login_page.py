from selenium.webdriver.common.by import By
from workbog.ranzhi_fun import RanZhi_Fun,PublicPage,ReadYaml,GetPath
from time import sleep

class Login_Page(PublicPage):
    ready_yaml = GetPath().get_path('tinyschool\\ele.yaml')
    def loginpage(self,url,username,password,yanzhengma):
        self.ready = ReadYaml().readyaml(self.ready_yaml)
        driver = self.driver
        self.read = self.ready['Login_Page']
        # 打开网站
        driver.open(url)
        sleep(1)
        # 点击登录
        driver.click(self.read['CLICK'])
        # 输入账号
        driver.input(self.read['USERNAME'],username)
        # 输入密码
        driver.input(self.read['PASSWORD'],password)
        #验证码
        driver.input(self.read['YANZHENGMA'],yanzhengma)
        # 确认登录
        driver.click(self.read['DENGLU'])
        # 选择角色
        sleep(2)
        driver.click(self.read['JUESE'])
        # sleep(2)
        # 关闭浏览器
        # self.driver.close()

    def loginsuccess_assert(self):
        sleep(3)
        self.driver.show_wait((By.LINK_TEXT, self.read['SHOWWAIT']))
        return self.driver.get_text(self.read['DUANYAN'])






if __name__ == '__main__':
    driver = RanZhi_Fun('Chrome')
    a = Login_Page(driver)
    a.loginpage("http://91vschool.cn/#/index","13720453467","qtjy123456","szjx")