import unittest
from common1.desired_caps1 import appium_desired#导入启动app的模块
import logging
from time import sleep
from common1.data_pz import data

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info(data["qd"])
        self.driver=appium_desired()#启动app

    def tearDown(self):
        logging.info(data["qd1"])
        sleep(5)
        self.driver.close_app()#close_app()是关闭app