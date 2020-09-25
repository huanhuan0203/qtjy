import unittest
import time
from time import sleep
from parameterized import parameterized
from pages.tongzhi_page import TongZhi_Page
from workbog.ranzhi_fun import RanZhi_Fun, Open_Cx, GetPath, SendLog


class TongZhiCase(unittest.TestCase):
    pat = GetPath()
    # 读取xlsx表
    excel_path = pat.get_path('tinyschool\\tinyschool.xlsx')
    # 日志
    log_path = pat.get_path('tinyschool\\gather\\logs\\ranzhi.log')
    #截图
    screen_path = pat.get_path('tinyschool\\gather\\screenshot')
    # 读取xlsx表中不同表的数据
    tongzhisuccess_data = Open_Cx().open_xlsx(excel_path,'tongzhisuccess')
    # loginfail_data = Open_Cx().open_xlsx(excel_path,'loginfail')
    # 生成日志
    log = SendLog(log_path)
    @classmethod
    def setUpClass(self):
        self.driver = RanZhi_Fun('Chrome')
        self.tongzhis = TongZhi_Page(self.driver)
        self.tongzhis.loginpage("http://0855.91vschool.cn/#/index","13450953452","qtjy123456")
    @parameterized.expand(tongzhisuccess_data)
    def test_tongzhi(self,biaoti,neirong,rename):
        try:
            self.tongzhis.fatongzhi_page(biaoti,neirong)
            sleep(3)
            self.tongzhis.yifa_tongzhi_page()
            self.tongzhis.yishou_tongzhi_page()
            act = self.tongzhis.tongzhisuccess_assert()
            print(act)
            self.assertIn(rename,act)
            self.log.info("登录成功用例--%s登录成功" % biaoti)
        except:
            self.log.error("登录成功用例--%s登录失败"%biaoti)
            self.driver.get_screenshot('%s/test_login_success_%s.png'%(self.screen_path,(time.strftime('%Y-%m-%d_%H-%M-%S'))))
            raise ValueError("出错了")

    # @parameterized.expand(loginfail_data)
    # def test_login_fail(self,url,username,password,tip):
    #     try:
    #         self.login.loginpage(url,username,password)
    #         sleep(3)
    #         act = self.login.login_fail_assert()
    #         self.assertIn(tip,act)
    #         self.log.info("登录成功用例--%s登录失败" % username)
    #         self.login.login_fail_out()
    #     except:
    #         self.log.error("登录成功用例--%s登录成功" % username)
    #         self.driver.get_screenshot(
    #             '%s/test_login_success_%s.png' % (self.screen_path, (time.strftime('%Y-%m-%d_%H-%M-%S'))))
    #         raise ValueError("出错了")

    @classmethod
    def tearDownClass(self):
        # pass
        self.driver.close()

if __name__ == '__main__':
    unittest.main()