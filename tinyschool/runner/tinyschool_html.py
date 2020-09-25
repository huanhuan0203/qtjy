import time
import unittest
from workbog.HTMLTestRunner import HTMLTestRunner
from workbog.ranzhi_fun import SendEmail,GetPath
class Ranzhi_Html:
    case_path = GetPath().get_path('tinyschool\\cases\\')
    reports_path = GetPath().get_path('tinyschool\\gather\\report')

    def runner(self):
        suite = unittest.TestSuite()
        # suite.addTests(unittest.TestLoader().discover(self.case_path, pattern='login_case.py'))
        suite.addTests(unittest.TestLoader().discover(self.case_path, pattern='tongzhi_case.py'))
        # suite.addTests(unittest.TestLoader().discover(self.case_path, pattern='addtext_case.py'))
        # suite.addTests(unittest.TestLoader().discover(self.case_path, pattern='projack_case.py'))

        t = time.strftime('%Y-%m-%d_%H-%M-%S')
        report_path = '%s/ranzhi_%s.html'%(self.reports_path,t)
        report_file = open(report_path,'wb')
        runner = HTMLTestRunner(report_file, title='微校园测试报告', description='这是一份微校园系统测试报告')
        runner.run(suite)
        # 邮箱
        SendEmail().sendemail(report_path, 'c1594548996@163.com', 'JUIFZIYOWSJFQYIG', '1594548996@qq.com','微校园报告')


if __name__ == '__main__':
    Ranzhi_Html().runner()