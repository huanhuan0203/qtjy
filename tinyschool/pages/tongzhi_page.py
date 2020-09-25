
from selenium.webdriver.common.by import By
from time import sleep
from pages.login_page import Login_Page
from workbog.ranzhi_fun import RanZhi_Fun


class TongZhi_Page(Login_Page):
    def fatongzhi_page(self,biaoti,neirong):
        driver = self.driver
        read = self.ready['TongZhi_Page']
        #  点击通知
        sleep(2)
        driver.click(read['DIANTONG'])
        sleep(2)
        # 点击发通知
        driver.click(read['FATING'])
        sleep(5)
        #  点击发送对象
        driver.click(read['DUIXIANG'])
        sleep(4)
        # driver.show_wait((By.LINK_TEXT, self.read['教师']))
        #  点击选择教师
        driver.click(read['JIAOSHI'])
        sleep(5)
        #  点击选择具体的教师
        driver.click(read['JAIOSHI1'])
        sleep(5)
         # 选择教师并确定
        driver.click(read['JIAOSHI2'])
        sleep(2)
        # 发送标题
        driver.input(read['BIAOTI'],biaoti)
        sleep(2)
        #  发送内容
        driver.input(read['NEIRONG'], neirong)
        sleep(3)
        #  点击发布
        driver.click(read['FABU'])

    def yifa_tongzhi_page(self):
        driver = self.driver
        read = self.ready['TongZhi_Page']
        #  点击通知
        # sleep(2)
        # driver.click(read['DIANTONG'])
        # 选择已发送通知
        sleep(2)
        driver.click(read['YIFA'])
        sleep(1)
        # 点击已发通知
        driver.click(read['YIFA1'])
        sleep(1)
        #  选择第一个通知
        driver.click(read['YIFA2'])
        sleep(1)
        #  返回
        driver.click(read['FANHUI'])

        # # 删除已发通知
        # # 选择已发送通知
        # sleep(2)
        # driver.click(read['YIFA'])
        # sleep(1)
        # # 点击已发通知
        # driver.click(read['YIFA1'])
        # sleep(1)
        # #  选择第一个通知
        # driver.click(read['YIFA2'])
        # # 点击删除
        # sleep(1)
        # driver.click(read['SHANCHU'])
        # # 确认删除
        # sleep(5)
        # driver.click(read['QUESHAN'])

    def yishou_tongzhi_page(self):
        driver = self.driver
        read = self.ready['TongZhi_Page']
        #  点击通知
        # sleep(2)
        # driver.click(read['DIANTONG'])
        # # 选择已发送通知
        sleep(2)
        driver.click(read['YISHOU'])
        sleep(1)
        # 点击已发通知
        driver.click(read['YISHOU1'])
        sleep(1)
        #  选择第一个通知
        driver.click(read['YISHOU2'])
        sleep(1)
        #  返回
        driver.click(read['FANHUI1'])

    def tongzhisuccess_assert(self):
        driver = self.driver
        read = self.ready['TongZhi_Page']
        sleep(3)
        # self.driver.show_wait((By.LINK_TEXT, self.read['SHOWWAIT']))
        return self.driver.get_text(read['TONGZHIDUANYAN'])
        # a = self.driver.get_text(self.read['TONGZHIDUANYAN'])
        # print(a)



if __name__ == '__main__':
    driver = RanZhi_Fun('Chrome')
    b = TongZhi_Page(driver)
    b.loginpage("http://0855.91vschool.cn/#/index","13450953452","qtjy123456")
    b.fatongzhi_page("sds","sadasd")
    b.yifa_tongzhi_page()
    b.yishou_tongzhi_page()
    b.tongzhisuccess_assert()







