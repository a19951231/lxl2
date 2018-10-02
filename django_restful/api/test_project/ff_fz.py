from selenium.common.exceptions import NoSuchElementException#导入此异常处理的包
import requests
import logging#导入log生成模块

class Jk():
    def get(self,base_url):
        try:
            self.r = requests.get(base_url)
        except (NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))
        else:
            return self.r

    def get1(self,base_url,auth1,a):
        try:
            self.r=requests.get(base_url+a,auth=auth1)
        except (NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))
        else:
            return self.r

    def post(self,base_url,form_data1,auth1,a):
        try:
            self.r = requests.post(base_url + a, data=form_data1, auth=auth1)
        except (NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))
        else:
            return self.r

    def delete(self,base_url,auth1,a):
        try:
            self.r=requests.delete(base_url+a,auth=auth1)
        except (NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))
        else:
            return self.r

    def patch(self,base_url,form_data,auth1,a):
        try:
            self.r=requests.patch(base_url+a,data=form_data,auth=auth1)
        except (NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))
        else:
            return self.r


