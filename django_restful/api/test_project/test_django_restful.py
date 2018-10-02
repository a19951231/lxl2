import requests#导入接口测试的模块
import unittest#导入用例框架
import yaml#导入yaml数据
import logging#导入log生成模块
from ff_fz import Jk#导入数据封装
from data_pz import data#导入data
from mysql_action import DB#导入数据库初始化模块
import sys
import logging.config

#引入日志配置文件
CON_LOG='log.conf'#把log.conf给予CON_LOG
logging.config.fileConfig(CON_LOG)#使用logging调用config.fileConfig()方法加载我们配置的日志文件
logging=logging.getLogger()#然后使用logging调用getLogger()，生产log对象普抓日志

path="D:\\django_restful\\api"
sys.path.append(path)

class UserTest(unittest.TestCase):#定义一个类继承unittest
    def setUp(self):#初始方法
        self.base_url=data['api']['ip']#接口地址
        self.auth=(data['auth']['zhhao'],data['auth']['mm'])#登陆账号，密码

    def test_1(self):
        '''数据初始化'''
        self.db = DB()
        self.db.test_cz()

    def test_001_no_auth2(self):
        '''没有登陆的查询的用例'''
        logging.info('test_001_no_auth2')
        self.b=Jk()
        r=self.b.get(self.base_url)
        result=r.json()

        self.assertEqual(result['detail'],data['test_001_no_auth2']['detail'])#断言

    def test_002_add_user3(self):
        '''添加数据用例'''
        logging.info('test_002_add_user3')
        form_data={'username':data['test_002_add_user3']['username'],'email':data['test_002_add_user3']['email']}
        self.b = Jk()
        a=data['a1']['a']
        r=self.b.post(self.base_url,form_data,self.auth,a)
        result=r.json()

        self.assertEqual(result['username'],data['test_002_add_user3']['username'])
        self.assertEqual(result['email'],data['test_002_add_user3']['email'])

    #
    def test_003_update_user4(self):
        '''更新email用例'''
        logging.info('test_003_update_user4')
        form_data={'email':data['test_003_update_user4']['email']}
        self.b = Jk()
        a=data['a1']['a1']
        r=self.b.patch(self.base_url,form_data,self.auth,a)
        result=r.json()

        self.assertEqual(result['email'],data['test_003_update_user4']['email'])

    def test_004_delete_user5(self):
        '''删除数据的用例'''
        logging.info('test_004_delete_user5')
        self.b = Jk()
        a=data['a1']['a2']
        r=self.b.delete(self.base_url,self.auth,a)
        #r=requests.delete(self.base_url+'/2/',auth=self.auth)

        self.assertEqual(r.status_code,204)

    def test_005_get_user6(self):
        '''查看数据的用例'''
        logging.info('test_005_get_user6')
        self.b = Jk()
        a=data['a1']['a1']
        r=self.b.get1(self.base_url,self.auth,a)
        #r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['username'],data['test_005_get_user6']['username'])
        #self.assertEqual(result['email'],'2018@163.com')


class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url = data['api']['ip1']  # 接口地址
        self.auth = (data['auth']['zhhao'], data['auth']['mm'])  # 登陆账号，密码


    def test_001_group_developer1(self):
        logging.info('test_001_group_developer1')
        self.b = Jk()
        a='/1/'
        r=self.b.get1(self.base_url,self.auth,a)
        #r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Developer')

    def test_002_add_group2(self):
        logging.info('test_002_add_group2')
        form_data={'name':'Pm'}
        self.b = Jk()
        a='/'
        r=self.b.post(self.base_url,form_data,self.auth,a)
        #r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Pm')

    def test_003_update_group3(self):
        logging.info('test_003_update_group3')
        form_data={'name':'Boss'}
        self.b = Jk()
        a='/2/'
        r=self.b.patch(self.base_url,form_data,self.auth,a)
        #r=requests.patch(self.base_url+'/2/',data=form_data,auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Boss')

    def test_004_delete_group4(self):
        logging.info('test_004_delete_group4')
        self.b = Jk()
        a='/1/'
        r=self.b.delete(self.base_url,self.auth,a)
        #r=requests.delete(self.base_url+'/1/',auth=self.auth)
        self.assertEqual(r.status_code,204)

if __name__ == '__main__':
    unittest.main()
