from BSTestRunner import BSTestRunner#导入用例生成模块
import unittest
import time

#pattern="taobou*.py"就是执行带有taobou名称的脚本
if __name__=="__main__":
    #存放报告的文件夹
    report_dir='../test_case'
    # 定义测试用例路径
    test_dir = '../report1'  # 把我们测试的脚本路径写进去
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    # pattern="taobou*.py"就是执行带有taobou名称的脚本
    #报告命名时间格式化
    now=time.strftime("%Y-%m-%d %H_%M_%S")#这里的y是年，m是月，d是天，H是小时，M是分，S是秒
    #报告文件完整路径
    report_name=report_dir+'/'+now+'test_result.html'
    #report_dir是路径，bg是时间，result.html是后缀名，这就是生成报告的名称

    with open(report_name,'wb')as f:#这里就是通过with open打开report_name这个报告，然后使用wb方式去写测试结果，f1是变量名称
        runner=BSTestRunner(stream=f,title=u"考研帮app测试报告",description=u'测试结果如下：')
        #title="Test Report"报告的名称，description='Test case result'报告的描述
        runner.run(discover)
    f.close()
#使用discover可以一次调用多个脚本
#test_dir被测试脚本的路径
#pattern脚本名称匹配规定
#unittest只执行test的用例，就是我们创建一个脚本，用例开头一定要test开头