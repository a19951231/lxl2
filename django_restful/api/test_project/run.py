import unittest
from HTMLTestRunner import HTMLTestRunner
import time,yaml
#from api.test_project.mysql_action import DB
import logging.config
import sys

path="D:\\django_restful\\api"
sys.path.append(path)
if __name__ == '__main__':
    #引入日志配置文件
    CON_LOG='log.conf'#把log.conf给予CON_LOG
    logging.config.fileConfig(CON_LOG)#使用logging调用config.fileConfig()方法加载我们配置的日志文件
    logging=logging.getLogger()#然后使用logging调用getLogger()，生产log对象普抓日志

    test_dir='.'
    report_dir='./reports'

    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_django_restful.py')

    now=time.strftime('%Y-%m-%d %H_%M_%S')
    report_name=report_dir+'/'+now+' test_report.html'

    with open (report_name,'wb') as f:
        runner=HTMLTestRunner(stream=f,title='API Test Report',description='Django Restful API Test Report')
        logging.info('=========Start API Test=============')
        runner.run(discover)
    f.close()