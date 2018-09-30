from common1.myunit import StartEnd
from businessView1.registerView import RegisterView1#调用此方法
from common1.data_pz import data#调用data模块
import unittest#调用用例框架
import logging
import random
from behave import given


class RegisterTest(StartEnd):

    @given(data["ts1"]["ts5"])
    def test_user_register_1(self):
        '''注册账号成功用例'''
        logging.info(data["ts1"]["ts2"])#打印日志
        l=RegisterView1(self.driver)
        username = "lxl" + "vv" + str(random.randint(1000, 9000))
        password = "lxl" + str(random.randint(1000, 9000))
        email = "lxl" + str(random.randint(1000, 9000)) + "@qq.com"
        self.assertTrue(l.register_action(username,password,email,data["cs"]["cs0"]))#作断言，如果此调用方法返回True就执行成功，如果是false就执行失败

if __name__=="__main__":
    unittest.main()

