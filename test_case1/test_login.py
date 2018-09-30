from common1.myunit import StartEnd
from businessView1.login1 import LoginView#调用此类
from common1.data_pz import data#调用data模块
from data1.mysq_lj import Mysql_kybzhh#导入此类
import unittest#调用用例框架
import logging
import ddt
from behave import given

@ddt.ddt
class RegisterTest(StartEnd):
    @ddt.data([data["ts1"]["ts3"], Mysql_kybzhh().shuju(1,1), Mysql_kybzhh().shuju(1,2), "'''正确的账号和密码的登录用例'''"], [data["ts1"]["ts3"],"", "", "'''账号，密码为空的登录用例'''"],
              [data["ts1"]["ts3"], Mysql_kybzhh().shuju(0,1),Mysql_kybzhh().shuju(0,2), "'''登录错误的账号密码的登录用例'''"])
    @ddt.unpack
    @given(data["ts1"]["ts4"])
    def test_user_register_1(self,a,b,c,d):
        d
        logging.info(a)
        l=LoginView(self.driver)
        l.login_action(b,c)
        self.assertTrue(l.check_loginStatus())#定义一个断言，如果返回True就执行用例成功，如果false就失败



if __name__=="__main__":
    unittest.main()