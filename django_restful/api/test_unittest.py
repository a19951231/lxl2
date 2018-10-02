import requests
import unittest

class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/Users'
        self.auth=('root','a19951231')

    def test_get_user(self):#查询用例，get是查看
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()
        print(result)

        self.assertEqual(result['username'],'root')
        self.assertEqual(result['email'],'466279653@qq.com')

    def test_add_user(self):#增加用户
         form_data={'username':'lxl66','email':'22@163.com','groups':'http://127.0.0.1:8000/Groups/4/',"id":"4"}
         r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
         result=r.json()
         print(result)

         self.assertEqual(result['username'],'lxl66')
         self.assertEqual(result['email'],'22@163.com')


    # def test_update_user(self):#修改某一个字段的用例，如：更新id，邮箱哈这些，patch是修改
    #     form_data={'email':'zx2018@163.com'}
    #     r=requests.patch(self.base_url+'/3/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['email'],'zxw2018@163.com')

    # def test_delete_user(self):#删除用例，delete是删除
    #     r=requests.delete(self.base_url+'/3/',auth=self.auth)
    #
    #     self.assertEqual(r.status_code,204)

    # def test_no_auth(self):#没有权限的查询用例
    #     r=requests.get(self.base_url)
    #     result=r.json()
    #
    #     self.assertEqual(result['detail'],'Authentication credentials were not provided.')


class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/Groups'
        self.auth=('root','a19951231')

    def test_group_developer(self):
        r=requests.get(self.base_url+'/7/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['detail'],'Not found.')

    # def test_add_group(self):
    #     form_data={'name':'Pm'}
    #     r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['name'],'Pm')

    # def test_update_group(self):
    #     form_data={'name':'Boss'}
    #     r=requests.patch(self.base_url+'/6/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['name'],'Boss')

    # def test_delete_group(self):
    #     r=requests.delete(self.base_url+'/6/',auth=self.auth)
    #     self.assertEqual(r.status_code,204)

if __name__ == '__main__':
    unittest.main()
