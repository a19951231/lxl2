import logging
from common1.desired_caps1 import appium_desired
from common1.commmon_fun import Common,NoSuchElementException
from common1.data_pz import data
import random

class RegisterView1(Common):

    def add_register_info(self,nobmer):
        logging.info(data["ts"]["ts20"])#打印日志
        self.find_element2(data["ys"][0]["id"],data["zlys"][0]["ys0"])#点击院校操作
        logging.info(data["ts"]["ts4"])#打印日志
        logging.info(data["ts"]["ts21"])  # 打印日志
        self.find_elements1(data["ys"][0]["id"],data["xxys"][0]["ys0"],nobmer)#点击院校地址
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts22"])  # 打印日志
        self.find_elements1(data["ys"][0]["id"],data["xxys"][1]["ys1"],nobmer)# 点击某个地区的院校
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts23"])  # 打印日志
        self.find_element2(data["ys"][0]["id"], data["zlys"][1]["ys1"])  # 点击选择目标专业操作
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts24"])  # 打印日志
        self.find_elements1(data["ys"][0]["id"], data["zyys"][0]["ys0"], nobmer)  # 点击主专业操作
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts25"])  # 打印日志
        self.find_elements1(data["ys"][0]["id"], data["zyys"][1]["ys1"], nobmer)  # 点击专业的子目录操作
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts26"])  # 打印日志
        self.find_elements1(data["ys"][0]["id"], data["zyys"][2]["ys2"], nobmer)#点击子目录专业的专业操作
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts27"])  # 打印日志
        self.find_element(data["ys"][0]["id"], data["zlys"][2]["ys2"])#点击进入按钮
        logging.info(data["ts"]["ts4"])  # 打印日志

    def check_register_status(self):
        self.check_market_ad()
        try:
            self.find_element(data["ys"][0]["id"],data["ys"][8]["woann"])#然后点击我的按钮，跳转到我的的页面
            self.find_element2(data["ys"][0]["id"],data["ys"][9]["username"])#在我的页面里判断是否有这个用户名称元素存在
        except (NoSuchElementException,Exception) as e:#获取不了try里面的元素会执行下面的操作
            logging.error('错误原因为: %s' % str(e))#报错
            self.getScreenShot(data["ts"]["ts28"])#进行截图操作
            return False#返回false
        else:#如果存在就执行下面的代码
            logging.info(data["ts"]["ts8"])#打印日志
            return True#返回true

    def register_action(self,register_username,register_password,register_email,nobmer):#注册用户操作1
        self.check_cancelBtn()#点击引导页面的发现新版的弹框的取消按钮方法
        self.check_skipBtn()#点击app引导页面右上角按钮方法
        logging.info(data["ts"]["ts4"])#打印日志
        self.find_element(data["ys"][0]["id"],data["ys"][12]["zhucie"])#点击注册按钮
        logging.info(data["ts"]["ts11"])#打印日志
        logging.info(data["ts"]["ts12"])
        self.find_element(data["ys"][0]["id"],data["zhuys"][0]["ys0"])#点击添加头像按钮
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts12"])  # 打印日志
        self.find_elements1(data["ys"][0]["id"],data["zhuys"][1]["ys1"],nobmer)#选择图片操作
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts14"])  # 打印日志
        self.find_element(data["ys"][0]["id"],data["ys"][2]["ys2"])#点击保存按钮操作
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts15"])  # 打印日志
        self.find_element1(data["ys"][0]["id"],data["ys"][3]["ys3"],register_username)#输入用户账号操作
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts16"])  # 打印日志
        self.find_element1(data["ys"][0]["id"],data["ys"][4]["ys4"],register_password)#输入用户密码操作
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts17"])  # 打印日志
        self.find_element1(data["ys"][0]["id"],data["ys"][5]["ys5"],register_email)  # 输入邮箱操作
        logging.info(data["ts"]["ts4"])  # 打印日志
        logging.info(data["ts"]["ts18"])  # 打印日志
        self.find_element(data["ys"][0]["id"],data["ys"][6]["ys6"])#点击注册按钮操作
        logging.info(data["ts"]["ts4"])  # 打印日志

        try:
            self.find_element2(data["ys"][0]["id"],data["zlys"][0]["ys0"])#获取此元素作判断
        except (NoSuchElementException,Exception) as e:#如果找不到此元素会执行下面的操作
            logging.error("错误原因：%s"%str(e))#打印日志
            self.getScreenShot(data["ts"]["ts19"])#进行截图操作
            return False#并且返回false
        else:#如果找到此元素会执行下面的操作
            self.add_register_info(nobmer)
            if self.check_register_status():
                return True
            else:
                return  False

if __name__=="__main__":
    driver=appium_desired()
    register=RegisterView1(driver)
    username="lxl"+"vv"+str(random.randint(1000,9000))
    password="lxl"+str(random.randint(1000,9000))
    email="lxl"+str(random.randint(1000,9000))+"@qq.com"
    register.register_action(username,password,email,2)
